from purplevoter import model
from purplevoter.controllers.common import to_json, json_error, geocode_address
from purplevoter.controllers.common import get_mcommons_districts
from purplevoter.controllers.common import search_races
from purplevoter.controllers.common import get_all_races_for_city
from purplevoter.lib.base import BaseController, render
from purplevoter.model import meta
from pylons import request, response
from pylons import tmpl_context as c
from pylons.controllers.util import abort, redirect_to, redirect
from pylons.decorators.cache import beaker_cache
from pylons.decorators.rest import dispatch_on
from sqlalchemy.orm.exc import NoResultFound
import datetime
import logging
import simplejson as json

logger = logging.getLogger(__name__)



    
class PeopleController(BaseController):

    def index(self):
        """ Home page """
        return render('index.mako')

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
            addresses = [address[0] for address in c.address_matches]
            return json_error(400, "Ambiguous address", data=addresses)
        return json.dumps(c.races, sort_keys=True, indent=1, default=to_json)

    def _search(self):
        """Find districts and people, given an address."""
        lat = lon = None
        c.races = []
        c.districts = []
        c.search_term = request.params.get('address', '')

        # XXX parameterize the election.
        election_date = datetime.date(2009, 9, 15)
        election_stagename = 'Primary'
        election_name = u'New York City 2009'
        election_q = meta.Session.query(model.Election)
        c.election = election_q.filter_by(date=election_date,
                                          stagename=election_stagename,
                                          name=election_name).one()

        c.status = request.params.getall('status')

        all_levels = ('federal', 'state', 'city')
        level_names = request.params.getall('level_name') or all_levels

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
            # what state we're in.  (Geocoding doesn't tell us.)
            c.districts = get_mcommons_districts(c.lat, c.lon)
            # Assume all districts are in the same state.
            c.state = c.districts[c.districts.keys()[0]]['state']
            races = search_races(c)  #election, c.lon, c.lat, districts, level_names)
        elif request.params.has_key('city'):
            # Get all local info for the whole city.
            level_names = 'city'
            races = get_all_races_for_city(request.params.get('city'),
                                           c.election)
        else:
            races = []

        c.races = races
        # At least for the html view, it's nice to group by districts.
        # but not sure about this yet.
        districts = set([r.district for r in races])
        sortkey = lambda d: (d['district_name'], d['district_type'])
        c.districts = sorted(districts, key=sortkey)

        

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

