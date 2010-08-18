from whoismygov import model
from whoismygov.model import meta
from pylons import config
from pylons import request, response
from pylons.decorators.cache import beaker_cache
from sqlalchemy.exc import UnboundExecutionError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import func
import datetime
import geopy
import simplejson as json
import urllib2

def to_json(obj):
    if isinstance(obj, datetime.date) or isinstance(obj, datetime.datetime):
        return obj.isoformat()
    elif isinstance(obj, model.People):
        info = {'fullname': obj.fullname}
        if obj.incumbent_office:
            info['incumbent_office'] = obj.incumbent_office
            info['incumbent_district'] = obj.incumbent_district.district_name
        for m in obj.meta:
            info[m.meta_key] = m.meta_value
        return info
    elif isinstance(obj, model.Race):
        try:
            incumbents = obj.incumbents
        except UnboundExecutionError:
            incumbents = meta.session.merge(obj.incumbents, dont_load=True)
        info = {'district_name': obj.district.district_name,
                'district_type': obj.district.district_type,
                'level_name': obj.district.level_name,
                'state': obj.district.state,
                'office': obj.office,
                'election': obj.election.name,
                'election_stagename': obj.election.stagename,
                'election_date': obj.election.date,
                'candidates': sorted(obj.candidates, key=lambda x: x.fullname),
                'incumbents': sorted(obj.incumbents, key=lambda x: x.fullname),
                'parent_district_name': obj.district.parent_district_name,
                }
        return info
    else:
        raise TypeError

    
def json_error(status, reason, data=None):
    # Not sure of the best way to do custom error responses.
    # Calling abort(400) seems to trigger the default error-handling 
    # middleware which spits out HTML.  This works okay:
    response.status = status
    request.environ['pylons.status_code_redirect'] = True
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'error': reason, 'error_data': data})    

@beaker_cache(expire=607, type='memory')
def geocode_address(address):
   """ convert an address string into a list of (addr_str, (lat,lon))
   tuples """
   # move

   if config.get('mock_geocoder'):
       # Intended for use in testing.
       address_gen = request.environ['mockgeocoder.results']
   else:
       google_api_key = config['google_api_key']
       geocoder = geopy.geocoders.Google(api_key=google_api_key)
       address_gen = geocoder.geocode(address, exactly_one=False)
   result = [(addr, (lat, lon)) for addr, (lat, lon) in address_gen]
   #print result
   return result

@beaker_cache(expire=613, type='memory')
def get_mcommons_districts(lat, lon):
    """ takes a lat, lon and returns a data
    structure representing legislative districts (and any other
    info mcommons has about those districts?)
    """
    # XXX This cannot handle local districts, mcommons doesn't
    # support those.
    apiurl = 'http://congress.mcommons.com/districts/lookup.json?lat=%s&lng=%s' % (lat, lon)

    # First we pull out the available districts.

    # XXX need to handle network failures!!
    districts = json.loads(urllib2.urlopen(apiurl).read())

    # Clean up keys we don't need
    for key in 'lat', 'lng':
        try:
            del districts[key]
        except KeyError:
            pass

    assert districts, "Got no districts?"
    return districts


def search_races(context):
    """Find all races
    """
    election = context.election
    lon = context.lon
    lat = context.lat
    level_names = context.level_names
    districts = context.districts
    state = context.state
    
    result_races = []

    if not districts:
        return result_races

    race_q = meta.Session.query(model.Race).filter_by(election=election)

    # Get US Senate races.
    if 'federal' in level_names:
        senate_districts = get_us_senator_districts(state)
        for sd in senate_districts:
            races = race_q.filter_by(district=sd).all()
            result_races.extend(races)

    # Get statewide and US House races.
    for level_type in districts:
        #change the mcommons parameters to votesmart parameters
        try:
            district_name = "District " + str(int(districts[level_type]['district']))
        except ValueError:
            district_name = "District " + districts[level_type]['district']

        level_name = ""
        if level_type == 'federal':
            level_name = "Federal"
            district_type = "U.S. House"
        elif level_type == 'state_upper':
            level_name = "State"
            district_type = "State Senate"
        elif level_type == 'state_lower':
            level_name = "State"
            district_type = "State Assembly"

        if level_name.lower() not in level_names:
            continue

        district = get_district_for_state(state, district_name, district_type)
        races = race_q.filter_by(district=district).all()
        result_races.extend(races)

    # Merge in local data.
    if 'city' in level_names:
        point = "POINT(%.20f %.20f)" % (lon, lat)
        district_q = meta.Session.query(model.Districts)
        district_q = district_q.filter(
            func.st_contains(
                model.Districts.geometry, 
                func.ST_GeomFromText(point, meta.storage_SRID)))
#        district_q = filter_people_by_status(district_q, status=())
        local_districts = district_q.all()
        result_races.extend(get_races_for_districts(local_districts, election))

    return result_races  # list(set(result_races))?


def get_us_senator_districts(state):
    district_q = meta.Session.query(model.Districts)
    district_q = district_q.filter(model.Districts.state==state).\
        filter(model.Districts.level_name=="Federal").\
        filter(model.Districts.district_type=="U.S. Senate")
    # Confusingly, we have 3 extra senate districts, apparently to
    # distinguish senators by classes (see
    # http://en.wikipedia.org/wiki/Us_senate#Elections_and_term).
    # Ignore those for now.
    district_q = district_q.filter(
        model.Districts.district_name.endswith('Seat'))
    district_q = filter_people_by_status(district_q, status=())
    fed_districts = district_q.all()
    return fed_districts

def filter_people_by_status(query, status):
    # XXX I don't remember what this was for!
    return query
#      """Filter a People query to return only results that have an
#     associated PeopleMeta entry whose meta_key is in the `status`
#     list and meta_value is 'true'."""
#     if not status:
#         return query
#     query = query.join(model.People, model.PeopleMeta).filter(and_(
#             model.PeopleMeta.meta_key.in_(status),
#             model.PeopleMeta.meta_value=='true'))
#     return query


def get_races_for_districts(districts, election):
    # XXX This doesn't work and I don't understand the sqlalchemy error...
    #    races = race_q.filter(model.Race.district.in_(local_districts))
    #    result_races.extend(races)
    # So instead, I iterate, thereby spewing a ton of db queries.
    # Performance will be horrible, but it works.
    result_races = []
    for dist in districts:
        for race in dist.races:
            if race.election == election:
                result_races.append(race)
    return result_races


def get_district_for_state(state, district_name, district_type, status=()):
    district_q = meta.Session.query(model.Districts)
    district_q = district_q.filter(model.Districts.state==state)
    district_q = district_q.filter(model.Districts.district_name==district_name)
    district_q = district_q.filter(model.Districts.district_type==district_type)
    district_q = filter_people_by_status(district_q, status=())
    try:
        result = district_q.one()
        return result
    except NoResultFound:
        return None


@beaker_cache(expire=617, type='memory')
def get_all_races_for_city(self, city_name, election):
    city_q = meta.Session.query(model.Districts)
    # XXX This will need disambiguation when we go beyond NYC.
    city_q = city_q.filter_by(district_type='City', district_name=city_name)
    city = city_q.one()

    # Get ALL the districts within this city.
    district_q = meta.Session.query(model.Districts)
    # For some reason I get a ProgrammingError if I just pass city.geometry
    # as an arg to func.st_within().  Hackaround: pass it as a string.
    # This is horribly inefficient, but no more so than the rest of my queries...
    city_geom = city.geometry.wkt
    district_q = district_q.filter(
        func.st_within(model.Districts.geometry,
                       func.ST_GeomFromText(city_geom,
                                            meta.storage_SRID)))
    districts = district_q.all()

    races = get_races_for_districts(districts, election)
    return races
