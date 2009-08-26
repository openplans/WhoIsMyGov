from purplevoter import model
from purplevoter.lib.base import BaseController, render
from purplevoter.model import meta
from pylons import config
from pylons import request, response
from pylons import tmpl_context as c
from pylons.controllers.util import abort, redirect_to, redirect
from pylons.decorators.cache import beaker_cache
from pylons.decorators.rest import dispatch_on
from sqlalchemy.exc import UnboundExecutionError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import func
from sqlalchemy import and_
import datetime
import geopy
import logging
import simplejson as json
import urllib2

log = logging.getLogger(__name__)


def _to_json(obj):
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
                }
        return info
    else:
        raise TypeError



class PeopleController(BaseController):

    def search(self):
        """public HTML search page"""
        self._search()
        s = render('search_form.mako', cache_expire=599, cache_type='memory', 
                   cache_key='%s %s' % (request.method, request.url))
        return s

    @beaker_cache(expire=601, type="memory", query_args=True)
    # could use @jsonify but i like more control of the output.
    def search_json(self):
        """pseudo-REST public search service.
        (pseudo because there's no hypermedia here.)
        """
        self._search()
        response.headers['Content-Type'] = 'application/json'
        if len(c.address_matches) > 1:
            # XXX need to advise the client that this is ambiguous.
            c.races = []
        return json.dumps(c.races, sort_keys=True, indent=1, default=_to_json)

    def _search(self):
        """Find districts and people, given an address."""
        lat = lon = None
        c.races = []
        c.districts = []
        c.search_term = request.params.get('address', '')
        c.election_date = datetime.date(2009, 9, 15)
        c.election_stagename = 'Primary'  # XXX parameterize this.
        c.election_name = u'New York City 2009'  # XXX parameterize this.
        c.status = request.params.getall('status')
        all_levels = ('federal', 'state', 'city')
        level_names = request.params.getall('level_name') or all_levels
        if request.params.has_key('lat') and request.params.has_key('lon'):
            lat = request.params['lat']
            lon = request.params['lon']
        elif request.params.has_key('address'):
            address_matches = self._geocode_address(request.params['address'])
            if len(address_matches) == 1:
                addr_str, (lat, lon) = address_matches[0]
            elif len(address_matches) > 1:
                # Let the user figure it out
                c.address_matches = address_matches
                return
            else:
                # XXX signal an error?
                c.address_matches = []
                return
        # We should have a location to work with now.
        if lat and lon:
            c.lat, c.lon = float(lat), float(lon)
            # We need the mcommons district lookup no matter which
            # levels we care about, because that's how we find out
            # what state we're in.  (Geocoding doesn't tell us.)
            districts = self._get_mcommons_districts(c.lat, c.lon)
            races = self._search_races(districts, level_names)
        elif request.params.has_key('city'):
            # Get all local info for the whole city.
            level_names = 'city'
            races = self._get_all_races_for_city(request.params.get('city'))
        else:
            races = []

        c.races = races
        # At least for the html view, it's nice to group by districts.
        # but not sure about this yet.
        districts = set([r.district for r in races])
        sortkey = lambda d: (d.district_name, d.district_type)
        c.districts = sorted(districts, key=sortkey)


    @beaker_cache(expire=607, type='memory')
    def _geocode_address(self, address):
       """ convert an address string into a list of (addr_str, (lat,lon))
       tuples """
       # move

       if config.get('mock_geocoder'):
           address_gen = request.environ['mockgeocoder.results']
       else:
           google_api_key = config['google_api_key']
           geocoder = geopy.geocoders.Google(api_key=google_api_key)
           address_gen = geocoder.geocode(address, exactly_one=False)
       result = [(addr, (lat, lon)) for addr, (lat, lon) in address_gen]
       #print result
       return result


    def _search_races(self, districts, level_names):
        """Find all races for the given district ids
        """
        result_races = []

        if not districts:
            return result_races

        state = districts[districts.keys()[0]]['state']

        election = self._get_election_from_request()

        if 'federal' in level_names:
            # XXXGet senatorial candidates
            pass

        for level_type in districts:
            #change the mcommons parameters to votesmart parameters
            #name of the district
            try:
                district_name = "District " + str(int(districts[level_type]['district']))
            except ValueError:
                district_name = "District " + districts[level_type]['district']

            level_name = ""
            #name of level
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

            # Statewide races.
            district = self._get_district_for_state(state, district_name, district_type)
            race_q = meta.Session.query(model.Race)
            race_q = race_q.filter_by(election=election)
            races = race_q.filter_by(district=district).all()
            result_races.extend(races)

        # Merge in local data.
        if 'city' in level_names:
            point = "POINT(%.20f %.20f)" % (c.lon, c.lat)
            district_q = meta.Session.query(model.Districts)
            district_q = district_q.filter(
                func.st_contains(
                    model.Districts.geometry, 
                    func.ST_GeomFromText(point, meta.storage_SRID)))
            district_q = self._filter_people_by_status(district_q)
            local_districts = district_q.all()
            result_races.extend(self._get_races_for_districts(local_districts))

        return result_races  # list(set(result_races))?


    def _get_races_for_districts(self, districts):
        # XXX This doesn't work and I don't understand the sqlalchemy error...
#             races = race_q.filter(model.Race.district.in_(local_districts))
#             result_races.extend(races)
        # So instead, I iterate, thereby spewing a ton of db queries.
        # Performance will be horrible, but it works.
        election = self._get_election_from_request()
        result_races = []
        for dist in districts:
            for race in dist.races:
                if race.election == election:
                    result_races.append(race)
        return result_races


    @beaker_cache(expire=613, type='memory')
    def _get_mcommons_districts(self, lat, lon):
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


    @staticmethod
    def _filter_people_by_status(query):
        if not c.status:
            return query
        query = query.join(model.People, model.PeopleMeta).filter(and_(
                model.PeopleMeta.meta_key.in_(c.status),
                model.PeopleMeta.meta_value=='true'))
        return query


    def _get_us_senator_districts(self, state):
        district_q = meta.Session.query(model.Districts)
        district_q = district_q.filter(model.Districts.state==state).\
            filter(model.Districts.level_name=="Federal").\
            filter(model.Districts.district_type=="U.S. Senate")
        district_q = self._filter_people_by_status(district_q)
        fed_districts = district_q.all()
        return fed_districts

    def _get_district_for_state(self, state, district_name, district_type):
        district_q = meta.Session.query(model.Districts)
        district_q = district_q.filter(model.Districts.state==state)
        district_q = district_q.filter(model.Districts.district_name==district_name)
        district_q = district_q.filter(model.Districts.district_type==district_type)
        district_q = self._filter_people_by_status(district_q)
        try:
            result = district_q.one()
            return result
        except NoResultFound:
            return None

    def _get_election_from_request(self):
        election_q = meta.Session.query(model.Election)
        election = election_q.filter_by(date=c.election_date,
                                        stagename=c.election_stagename,
                                        name=c.election_name).one()
        return election

    @beaker_cache(expire=617, type='memory')
    def _get_all_races_for_city(self, city_name):
        city_q = meta.Session.query(model.Districts)
        # XXX This will need disambiguation when we go beyond NYC.
        city_q = city_q.filter_by(district_type='City', district_name=city_name)
        city = city_q.one()

        election = self._get_election_from_request()

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

        races = self._get_races_for_districts(districts)
        return races

        

    #######################################################################
    # Metadata UI handlers
    #######################################################################

    def add_meta(self):
        """Add an arbitrary key/value pair to the information about
        a district."""
        abort(403)  # Disabling this until we have a plan for auth & moderation.

        if request.method not in ('POST', 'PUT'):
            abort(405)
            #XXX add header information about allowed methods
        districts_q = meta.Session.query(model.Districts)
        try:
            district = districts_q.filter(model.Districts.id == request.params.get('district_id')).one()
            district_meta = model.DistrictsMeta()
            district_meta.meta_key = request.params.get('meta_key')
            district_meta.meta_value = request.params.get('meta_value')
            district.meta.append(district_meta)
            meta.Session.commit()
            redirect_to(request.referrer)
        except (KeyError, NoResultFound):
            abort(400)

    @dispatch_on(POST="_do_update_meta")
    def update_meta(self, meta_id):
        abort(403)  # Disabling this until we have a plan for auth & moderation.

        c.district_meta = meta.Session.query(model.DistrictsMeta).filter(model.DistrictsMeta.id == meta_id).one()
        c.referrer = request.referrer
        return render('/edit_meta.mako') 
   
    def _do_update_meta(self, meta_id):
        district_meta = meta.Session.query(model.DistrictsMeta).filter(model.DistrictsMeta.id == meta_id).one()
        district_meta.meta_key = request.params.get('key')
        district_meta.meta_value = request.params.get('value')
        meta.Session.commit()
        redirect(request.params.get('referrer')) 

    @dispatch_on(POST="_do_delete_meta")
    def delete_meta(self, meta_id):
        abort(403)  # Disabling this until we have a plan for auth & moderation.

        c.district_meta = meta.Session.query(model.DistrictsMeta).filter(model.DistrictsMeta.id == meta_id).one()
        c.referrer = request.referrer
        return render('/delete_meta.mako') 

    def _do_delete_meta(self, meta_id):
        district_meta = meta.Session.query(model.DistrictsMeta).filter(model.DistrictsMeta.id == meta_id).one()
        meta.Session.delete(district_meta)
        meta.Session.commit()
        redirect(request.params.get('referrer')) 

