import logging

from pylons import request, response, session, tmpl_context as c
from pylons import config
from pylons.controllers.util import abort, redirect_to

from purplevoter.lib.base import BaseController, render

import geopy

import formencode
from formencode import Schema, Invalid
from formencode import validators, compound
from pyquery import PyQuery as Q
from lxml import etree

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
            lat, lon = self._geocode_address(request.params['address'])
            c.people = self._get_districts(lat, lon)
        
        return render('search_form.mako')

    def _geocode_address(self, address):
       """ convert string address into a lat, long tuple """
       # move
       google_api_key = config['google_api_key']
       geocoder = geopy.geocoders.Google(api_key=google_api_key)
       addr_str, (lat, lon) = geocoder.geocode(address)

       return lat, lon

    def _get_districts(self, lat, lon):
        """ takes a lat, lon and returns a list of elected officials
        and  any candidates running for office in districts serving
        that location """
        # Rewrite the pyquery out of this, it's so ugly, it ain't pythonic
        apiurl = 'http://congress.mcommons.com/districts/lookup.xml?lat=%s&lng=%s' % (lat, lon)

        # First we pull out the available districts.
        districts = dict(Q(etree.parse(apiurl).getroot())('federal, state_upper, state_lower').map(lambda i, e: (e.tag, Q(e))))

        # Each of the valuse is a pyQuery object containing all of the district
        # data.  Let's turn it into a dict
        for district in districts:
            districts[district] = dict(districts[district].find('*').map(lambda i, e: (e.tag, Q(e).text())))

        return districts
