from purplevoter import model
from purplevoter.lib.base import BaseController, render
from purplevoter.model import meta
from pylons import config
from pylons import request, response
from pylons import tmpl_context as c
from pylons.controllers.util import abort, redirect_to, redirect
from pylons.decorators.rest import dispatch_on
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import func
import geopy
import logging
import simplejson as json
import urllib2

log = logging.getLogger(__name__)

class PeopleController(BaseController):

    def search(self):
        """public HTML search page"""
        self._search()
        import pdb; pdb.set_trace()
        s = render('search_form.mako')
        return s


    # could use @jsonify but i like more control of the output.
    
    def search_json(self):
        """pseudo-REST public search service.
        (pseudo because there's no hypermedia here.)
        """
        self._search()
        output = []
        for district in c.districts:
            people = []
            for p in district.people:
                person_info = {'fullname': p.fullname}
                for m in p.meta:
                    person_info[m.meta_key] = m.meta_value
                people.append(person_info)

            output.append({'district_name': district.district_name,
                           'district_type': district.district_type,
                           'level_name': district.level_name,
                           'state': district.state,
                           'people': people,
                           })
        response.headers['Content-Type'] = 'application/json'
        return json.dumps(output, sort_keys=True, indent=1)


    def _search(self):
        """Find districts and people, given an address."""
        lat = lon = None
        c.search_term = request.params.get('address', '')
        if request.params.has_key('lat') and request.params.has_key('lon'):
            c.lat = request.params['lat']
            c.lon = request.params['lon']
        elif request.params.has_key('address'):
            address_matches = self._geocode_address(request.params['address'])
            if len(address_matches) == 1:
                addr_str, (lat, lon) = address_matches[0]
                
            elif len(address_matches) > 1:
                # Let the user figure it out
                c.address_matches = address_matches
            else:
                # XXX signal an error
                return
        if lat and lon:
            c.lat, c.lon = lat, lon
            # We need the mcommons district lookup no matter which
            # levels we care about, because that's how we find out
            # what state we're in.  (Geocoding doesn't tell us.)
            districts = self._get_mcommons_districts()
            all_levels = ('federal', 'state', 'city')
            level_names = request.params.getall('level_name') or all_levels
            c.districts = self._do_search(districts, level_names)
    

    def _geocode_address(self, address):
       """ convert an address string into a list of (addr_str, (lat,lon))
       tuples """
       # move
       google_api_key = config['google_api_key']
       geocoder = geopy.geocoders.Google(api_key=google_api_key)
       address_gen = geocoder.geocode(address, exactly_one=False)
       return [(addr, (lat, lon)) for addr, (lat, lon) in address_gen]


    def _do_search(self, districts, level_names):
        return_districts = []

        if not districts:
            return return_districts

        #mcommons doesn't return 'federal_upper', so first manually add this

        state = districts[districts.keys()[0]]['state']

        if 'federal' in level_names:
            return_districts.extend(self._get_us_senator_districts(state))

        for level_type in districts:

            #change the mcommons parameters to votesmart parameters
            
            #name of the state
            state = districts[level_type]['state']
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

            import pdb; pdb.set_trace()
            dstr = self._get_district_for_state(state, district_name, district_type)
            if not dstr:
                continue

            for person in dstr.people:
                print person.fullname


            return_districts.append(dstr)

        # Merge in local data.
        if 'city' in level_names:
            point = "POINT(%.20f %.20f)" % (c.lon, c.lat)
            district_q = meta.Session.query(model.Districts)
            local_districts = district_q.filter(
                func.st_contains(
                    model.Districts.geometry, 
                    func.ST_GeomFromText(point, meta.storage_SRID))).all()
            return_districts.extend(local_districts)

        return_districts = [d for d in return_districts if len(d.people) != 0]
        return return_districts
        
    def _get_mcommons_districts(self):
        """ takes a lat, lon from the context and returns a data
        structure representing legislative districts (and any other
        info mcommons has about those districts?)
        """
        # XXX This cannot handle local districts, mcommons doesn't
        # support those.
        apiurl = 'http://congress.mcommons.com/districts/lookup.json?lat=%s&lng=%s' % (c.lat, c.lon)

        # First we pull out the available districts.
        districts = json.loads(urllib2.urlopen(apiurl).read())

        # Clean up keys we don't need
        for key in 'lat', 'lng':
            try:
                del districts[key]
            except KeyError:
                pass

        assert districts, "Got no districts?"
        return districts


    def _get_us_senator_districts(self, state):
        district_q = meta.Session.query(model.Districts)
        fed_districts = district_q.filter(model.Districts.state==state).\
                              filter(model.Districts.level_name=="Federal").\
                              filter(model.Districts.district_type=="U.S. Senate").\
                              all()
        return fed_districts

    def _get_district_for_state(self, state, district_name, district_type):
        district_q = meta.Session.query(model.Districts)
        district_q = district_q.filter(model.Districts.state==state)
        district_q = district_q.filter(model.Districts.district_name==district_name)
        district_q = district_q.filter(model.Districts.district_type==district_type)
        try:
            result = district_q.one()
            return result
        except NoResultFound:
            return None
        
 

    ################################################################################
    # Metadata UI handlers
    ################################################################################

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
