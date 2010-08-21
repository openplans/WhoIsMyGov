from pylons import request, response
from pylons import tmpl_context as c
from pylons.controllers.util import abort, redirect_to, redirect
from pylons.decorators.cache import beaker_cache
from pylons.decorators.rest import dispatch_on
from sqlalchemy.orm.exc import NoResultFound
from whoismygov import model
from whoismygov.controllers.common import get_all_races_for_city
from whoismygov.controllers.common import get_mcommons_districts
from whoismygov.controllers.common import search_races
from whoismygov.controllers.common import to_json, json_error, geocode_address
from whoismygov.lib.base import BaseController, render
from whoismygov.model import meta
import datetime
import logging
import simplejson as json

logger = logging.getLogger(__name__)



    
class PeopleController(BaseController):


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

