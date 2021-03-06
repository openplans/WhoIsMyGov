from pylons import request, response
from pylons import tmpl_context as c
from pylons.controllers.util import abort
from pylons.decorators.cache import beaker_cache
from sqlalchemy.orm.exc import NoResultFound
from whoismygov import model
from whoismygov.controllers.common import geocode_address
from whoismygov.controllers.common import get_all_races_for_city
from whoismygov.controllers.common import get_mcommons_districts
from whoismygov.controllers.common import search_races
from whoismygov.controllers.common import to_json, json_error
from whoismygov.lib.base import BaseController, render
from whoismygov.model import meta
import datetime
import logging
import simplejson as json

logger = logging.getLogger(__name__)


class ElectionsController(BaseController):

    def index(self):
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

    def _get_election(self, name, stage, date):
        election_q = meta.Session.query(model.Election)
        try:
            election = election_q.filter_by(name=name, stagename=stage, date=date).one()
        except NoResultFound:
            abort(404)
        return election

    def view_election(self, name, stage, date):
        """info about an election, with address search results if
        address provided.
        """
        c.election = self._get_election(name, stage, date)
        self._search()
        s = render('search_form.mako', cache_expire=599, cache_type='memory', 
                   cache_key='%s %s' % (request.method, request.url))
        return s

    @beaker_cache(expire=601, type="memory", query_args=True)
    # could use @jsonify but i like more control of the output.
    def search_json(self, name=u'New York City 2009', stage=u'Primary',
                    date=datetime.date(2009, 9, 15)):
        """pseudo-REST public search service.
        (pseudo because there's no hypermedia here.)
        """
        c.election = self._get_election(name, stage, date)
        self._search()
        response.headers['Content-Type'] = 'application/json'
        if len(c.address_matches) > 1:
            addresses = [address[0] for address in c.address_matches]
            return json_error(400, "Ambiguous address", data=addresses)
        s = json.dumps(c.races, sort_keys=True, indent=1, default=to_json)
        return s

    def _search(self):
        """Find races, given c.election and an address or lonlat in
        the request."""

        lat = lon = None
        c.races = []
        c.districts = []
        c.search_term = request.params.get('address', '')
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
            races = get_all_races_for_city(request.params.get('city'),
                                           c.election)
        else:
            races = []

        c.races = races
        # At least for the html view, it's nice to group by districts.
        # but not sure about this yet.
        districts = set([r.district for r in races])
        sortkey = lambda d: (d.district_name, d.district_type)
        c.districts = sorted(districts, key=sortkey)
