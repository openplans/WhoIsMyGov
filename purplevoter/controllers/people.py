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
            c.districts = self._get_or_insert_districts(districts)
        return render('search_form.mako')

    def add_meta(self):
        if request.method == 'GET':
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

    def _get_or_insert_districts(self, districts):
        return_districts = []
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
                    return_districts.append(exists)
                except NoResultFound:
                    district = model.Districts()
                    district.level_type = level_type
                    district.level_id = level_id 
                    district.district_name = district_name
                    district_meta = model.DistrictsMeta()
                    district_meta.meta_key = 'district_number'
                    district_meta.meta_value = districts[level_type]['district']
                    district.meta.append(district_meta)
                    meta.Session.save(district)
                meta.Session.commit()
                return_districts.append(district)
            except: 
                meta.Session.rollback()

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
