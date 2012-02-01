import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to
from pylons import config

from whoismygov.lib.base import BaseController
from whoismygov.model import Districts, DistrictsMeta
from whoismygov.model import meta

log = logging.getLogger(__name__)

class AdminController(BaseController):

    def get_vs_districts(self):
        """Populate the district and district_meta tables with
        saved votesmart data from the vsdata directory, merged with federal
        officials' names from the votesmart api.

        XXX votesmart API key access is no longer free!!

        XXX this needs to be auth protected

        XXX meant to be run only for bootstrapping really, so I'm not
        sure why it needs a web UI.

        """
        import yaml
        from votesmart import votesmart

        votesmart.apikey = config['votesmart_api_key']

	# TODO don't assume current working directory
        f = open('vsdata/districts.yaml', 'r')
        states = yaml.load(f)
        f = open('vsdata/offices.yaml', 'r')
        offices = yaml.load(f)

        state = 'NY'
        for office in states[state]:
            for dist in states[state][office]:
                district_type = offices[office]['name']
                district_name = dist[0]
                level_name = offices[office]['level_name']
            
                readable_info = state + ":  " +  level_name + ":  " +  district_type + ":  " + district_name
                
                # Avoid duplicate entries. Hooray for meaningless primary keys.
                
                exists = meta.Session.query(Districts).filter_by(
                    state=state, district_type=district_type,
                    level_name=level_name, district_name=district_name).count()
                if exists:
                    print "Already have:", readable_info
                    continue

                print readable_info
                district = Districts()
                district.state = state
                district.district_type = district_type
                district.level_name = level_name
                district.district_name = district_name
                try:
                    official = votesmart.officials.getByDistrict(dist[1])[0]
                    district_meta = DistrictsMeta()
                    district_meta.meta_key = 'official'
                    district_meta.meta_value = official.firstName + " " + official.lastName 
                    district.meta.append(district_meta)
                    print "VOTESMART: YES"
                except:
                    print "VOTESMART: NO for %s" % str((district.state, district.district_type, district.level_name))
                
                meta.Session.save(district)

        meta.Session.commit()

        return 'done'
