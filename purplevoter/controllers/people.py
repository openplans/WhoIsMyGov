import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from purplevoter.lib.base import BaseController, render

import formencode
from formencode import Schema, Invalid
from formencode import validators, compound

log = logging.getLogger(__name__)

class SearchForm(Schema):
   allow_extra_fields = True
   address = validator.String(not_empty=True)

class PeopleController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/people.mako')
        # or, return a response
        return 'Hello World'

    def search(self):
        return render('search_form.mako')
