import logging

from pylons import request, response, session, tmpl_context as c
from pylons import config
from pylons.controllers.util import abort, redirect_to
from pylons.decorators import validate

from sqlalchemy.orm.exc import NoResultFound
from purplevoter.lib.base import BaseController, render
from purplevoter import model
from purplevoter.model import meta
import geopy

import formencode
from formencode import Schema, Invalid
from formencode import validators, compound
from lxml import html
from votesmart import votesmart

votesmart.apikey = config.get('votesmart_api_key', 'da3851ba595cbc0d9b5ac5be697714e0')
log = logging.getLogger(__name__)

class SearchForm(Schema):
   allow_extra_fields = True
   address = validators.String(not_empty=True)

class PeopleController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/people.mako')
        # or, return a response
        return 'Hello World'

    @validate(schema=SearchForm(), form='search', prefix_error=False)
    def search(self):
        lat = lon = None
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
            c.people = self._get_districts(lat, lon) 
            self._get_or_insert_district(c.people)
        return render('search_form.mako')

    def _get_or_insert_district(self, districts):
        district_q = meta.Session.query(model.Districts)
        for level_type in districts:
            level_id = districts[level_type]['state']
            district_name = districts[level_type]['display_name']
            try:
                try:
                    exists = district_q.filter(model.Districts.level_type == level_type)\
                                        .filter(model.Districts.level_id == level_id)\
                                        .filter(model.Districts.district_name == district_name)\
                                        .one()
                except NoResultFound:
                    district = model.Districts()
                    district.level_type = level_type
                    district.level_id = level_id 
                    district.district_name = district_name
                    meta.Session.save(district)
                meta.Session.commit()
            except:
                meta.Session.rollback()
        
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
