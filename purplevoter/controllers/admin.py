import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from purplevoter.lib.base import BaseController
from purplevoter.model import Districts, DistrictsMeta
from purplevoter.model import meta

log = logging.getLogger(__name__)

class AdminController(BaseController):

    def get_vs_districts(self):
        """Populate the district and district_meta tables with
        saved data from the vsdata directory, merged with federal
        officials' names from the votesmart api.

        XXX this needs to be auth protected
        """
        import yaml
        from votesmart import votesmart

        votesmart.apikey = 'cb1c972b7f3200e89aaeed59bc90aac1'

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
