import logging

from pylons import request, response, session, tmpl_context as c
from pylons import config
from pylons.controllers.util import abort, redirect_to

from purplevoter.lib.base import BaseController, render

import geopy

import formencode
from formencode import Schema, Invalid
from formencode import validators, compound
from lxml import html

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

    def search(self):
        if request.params.has_key('address'):
            address_matches = self._geocode_address(request.params['address'])
            if len(address_matches) == 1:
                addr_str, (lat, lon) = address_matches[0]
                c.people = self._get_districts(lat, lon)
            else: # multiple matches, ask user which is correct
                c.address_matches = [addr for addr, (lat, lon) in address_matches]
        
        return render('search_form.mako')

    def _geocode_address(self, address):
       """ convert an address string into a list of (addr_str, (lat,lon))
       tuples """
       # move
       google_api_key = config['google_api_key']
       geocoder = geopy.geocoders.Google(api_key=google_api_key)
       address_gen = geocoder.geocode(address, exactly_one=False)
       return [(addr, (lat, lon)) for addr, (lat, lon) in address_gen]


    def _get_districts(self, lat, lon):
        """ takes a lat, lon and returns a list of elected officials
        and  any candidates running for office in districts serving
        that location """
        apiurl = 'http://congress.mcommons.com/districts/lookup.xml?lat=%s&lng=%s' % (lat, lon)

        # First we pull out the available districts.

        root = html.parse(apiurl).getroot()
        districts = dict((x.tag, dict((y.tag, y.text) for y in x.cssselect('%s *'% x.tag))) for x in root.cssselect('federal, state_upper, state_lower'))

        # This would probably be more pythonic in multiple lines
        for district in districts:
            pass

        return districts
