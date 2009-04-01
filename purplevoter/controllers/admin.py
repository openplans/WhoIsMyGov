import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from purplevoter.lib.base import BaseController
from purplevoter.model import Districts, DistrictsMeta
from purplevoter.model import meta

log = logging.getLogger(__name__)

class AdminController(BaseController):

    def get_vs_districts(self):
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
                print state + ":  " +  offices[office]['level_name'] + ":  " +  offices[office]['name'] + ":  " + dist[0]  
                district = Districts()
                district.state = state
                district.district_type = offices[office]['name']
                district.level_name = offices[office]['level_name']
                district.district_name = dist[0]
                try:
                    official = votesmart.officials.getByDistrict(dist[1])[0]
                    district_meta = DistrictsMeta()
                    district_meta.meta_key = 'official'
                    district_meta.meta_value = official.firstName + " " + official.lastName 
                    district.meta.append(district_meta)
                except:
                    pass
                meta.Session.save(district)

        meta.Session.commit()

        return 'done'
