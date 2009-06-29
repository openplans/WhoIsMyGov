from lxml import html
from purplevoter import model
from purplevoter.lib.base import BaseController, render
from purplevoter.model import meta
from pylons import config
from pylons import request
from pylons import tmpl_context as c
from pylons.controllers.util import abort, redirect_to, redirect
from pylons.decorators.rest import dispatch_on
from votesmart import votesmart
import geopy
import logging

votesmart.apikey = config.get('votesmart_api_key', 'da3851ba595cbc0d9b5ac5be697714e0')
log = logging.getLogger(__name__)

class PeopleController(BaseController):

    def search(self):
        lat = lon = None
        c.search_term = request.params.get('address', '')
        if request.params.has_key('lat') and request.params.has_key('lon'):
            lat = request.params['lat']
            lon = request.params['lon']
        elif request.params.has_key('address'):
            address_matches = self._geocode_address(request.params['address'])
            if len(address_matches) == 1:
                addr_str, (lat, lon) = address_matches[0]
            else:
                c.address_matches = address_matches
        if lat and lon:
            districts = self._get_districts(lat, lon)
            c.districts = self._do_search(districts)
        return render('search_form.mako')

    def add_meta(self):
        """Add an arbitrary key/value pair to the information about
        a district."""
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
        except KeyError, NoResultFound:
           abort(400)

    @dispatch_on(POST="_do_update_meta")
    def update_meta(self, meta_id):
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
        c.district_meta = meta.Session.query(model.DistrictsMeta).filter(model.DistrictsMeta.id == meta_id).one()
        c.referrer = request.referrer
        return render('/delete_meta.mako') 

    def _do_delete_meta(self, meta_id):
        district_meta = meta.Session.query(model.DistrictsMeta).filter(model.DistrictsMeta.id == meta_id).one()
        meta.Session.delete(district_meta)
        meta.Session.commit()
        redirect(request.params.get('referrer')) 
 
    def _do_search(self, districts):
        return_districts = []
        district_q = meta.Session.query(model.Districts)
        
        #mcommons doesn't return 'federal_upper', so first manually add this
        state = districts[districts.keys()[0]]['state']
        fed_district = district_q.filter(model.Districts.state==state).\
                              filter(model.Districts.level_name=="Federal").\
                              filter(model.Districts.district_type=="U.S. Senate").\
                              all()
        for district in fed_district:
            if len(district.meta) != 0:
               return_districts.append(district)

        for level_type in districts:

            #change the mcommoms parameters to votesmart parameters
            
            #name of the state
            state = districts[level_type]['state']
            #name of the district
            try:
               district_name = "District " + str(int(districts[level_type]['district']))
            except:
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


            try: 
				exists = district_q.filter(model.Districts.state == state)\
            	                    .filter(model.Districts.district_name == district_name)\
            	                    .filter(model.Districts.district_type == district_type)\
            	                    .one()
            except:
                continue
                #abort(404)
            return_districts.append(exists)

        return return_districts
        
    def _geocode_address(self, address):
       """ convert an address string into a list of (addr_str, (lat,lon))
       tuples """
       # move
       google_api_key = config['google_api_key']
       geocoder = geopy.geocoders.Google(api_key=google_api_key)
       address_gen = geocoder.geocode(address, exactly_one=False)
       return [(addr, (lat, lon)) for addr, (lat, lon) in address_gen]

    def _get_people(self, districts):
        for district, info in districts.iteritems():
            info['officials'] = votesmart.officials.getByDistrict(info['district'])


    def _get_people(self, districts):
        for district, info in districts.iteritems():
            info['officials'] = votesmart.officials.getByDistrict(info['district'])

    def _get_districts(self, lat, lon):
        """ takes a lat, lon and returns a list of elected officials
        and  any candidates running for office in districts serving
        that location """
        apiurl = 'http://congress.mcommons.com/districts/lookup.xml?lat=%s&lng=%s' % (lat, lon)

        # First we pull out the available districts.

        root = html.parse(apiurl).getroot()

        error = root.cssselect('error')
        if error:
            raise error[0].text

        districts = dict((x.tag, dict((y.tag, y.text) for y in x.cssselect('%s *'% x.tag))) for x in root.cssselect('federal, state_upper, state_lower'))

        # This would probably be more pythonic in multiple lines
        for district in districts:
            pass

        return districts
