from whoismygov import model
from whoismygov.controllers.common import geocode_address
from whoismygov.controllers.common import get_mcommons_districts
from whoismygov.controllers.common import search_races
from whoismygov.lib.base import BaseController, render
from whoismygov.model import meta
from pylons import request
from pylons import tmpl_context as c
from pylons.controllers.util import abort
from sqlalchemy.orm.exc import NoResultFound
import logging

logger = logging.getLogger(__name__)


class ElectionsController(BaseController):

    def list(self):
        """public HTML listing of elections"""

        election_q = meta.Session.query(model.Election)
        elections = election_q.order_by(model.Election.date,
                                        model.Election.name,
                                        model.Election.stagename)
        c.elections = elections
        s = render('elections_list.mako', cache_expire=600,
                   cache_type='memory', 
                   cache_key='%s %s' % (request.method, request.url))
        return s

    def view_election(self, name, stage, date):
        election_q = meta.Session.query(model.Election)
        try:
            election = election_q.filter_by(name=name, stagename=stage, date=date).one()
        except NoResultFound:
            abort(404)
        self._search(election)
        return self.search()
            

    def search(self):
        """public HTML search page"""
        s = render('search_form.mako', cache_expire=599, cache_type='memory', 
                   cache_key='%s %s' % (request.method, request.url))
        return s

    def _search(self, election):
        """Find races, given an election and an address."""

        # XXX REFACTOR: duplicate of PeopleController._search()
        lat = lon = None
        c.races = []
        c.districts = []
        c.search_term = request.params.get('address', '')
        c.election = election
        c.status = request.params.getall('status')
        all_levels = ('federal', 'state', 'city')
        c.level_names = request.params.getall('level_name') or all_levels
        if request.params.has_key('lat') and request.params.has_key('lon'):
            lat = request.params['lat']
            lon = request.params['lon']
        elif request.params.has_key('address'):
            address_matches = geocode_address(request.params['address'])
            if len(address_matches) == 1:
                addr_str, (lat, lon) = address_matches[0]
            elif len(address_matches) > 1:
                # Let the user figure it out
                c.address_matches = sorted(address_matches)
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
            # what state we're in.  (Geocoding doesn't tell us, and it
            # might be a state that we don't have a shape for in our
            # db).  (Also, for some districts - the ones they cover -
            # we may not keep its geometry in our DB at all.)
            c.districts = get_mcommons_districts(c.lat, c.lon)
            # Assume all districts are in the same state.
            c.state = c.districts[c.districts.keys()[0]]['state']
            races = search_races(c)
        elif request.params.has_key('city'):
            # Get all local info for the whole city.
            c.level_names = 'city'
            # XXX this method does not exist
            races = self._get_all_races_for_city(request.params.get('city'))
        else:
            races = []

        c.races = races
        # At least for the html view, it's nice to group by districts.
        # but not sure about this yet.
        districts = set([r.district for r in races])
        sortkey = lambda d: (d.district_name, d.district_type)
        c.districts = sorted(districts, key=sortkey)
