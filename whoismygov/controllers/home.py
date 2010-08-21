from whoismygov.lib.base import BaseController, render

class HomeController(BaseController):

    def index(self):
        """ Home page """
        return render('index.mako')
