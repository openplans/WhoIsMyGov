"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from pylons import config
from routes import Mapper

def make_map():
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE

    map.connect('home', '/',  controller='home', action='index')

    #map.connect('/officials/', controller='people', action='search')

    # Legacy 2009 NYC Primary search service URL.
    # should redirect this?
    map.connect('search.json', '/search.json', controller='elections', action='search_json')

    # Candidate Metadata URIs.
    map.connect('add_meta', '/add_meta',  controller='people', action='add_meta')
    map.connect('update_meta', '/meta/:meta_id/update',  controller='people', action='update_meta')
    map.connect('delete_meta', '/meta/:meta_id/delete',  controller='people', action='delete_meta')
    map.connect('get_vs_districts', '/admin/vs_districts',  controller='admin', action='get_vs_districts')

    map.connect('/elections', '/elections/',
                controller='elections', action='index')

    map.connect('/elections/{name}-{stage}-{date}/search.json',
                controller='elections', action='search_json')

    map.connect('/elections/{name}-{stage}-{date}',
                controller='elections', action='view_election')

    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')

    return map
