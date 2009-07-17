from sqlalchemy import *
from migrate import *

import os.path
import csv

def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.

    from purplevoter.model import People, Districts, PeopleMeta, meta
    meta.metadata.bind = migrate_engine

    csv_path = os.path.join(os.path.dirname(__file__), 'citycouncil_20090716.csv')
    reader = csv.DictReader(open(csv_path, 'r'), skipinitialspace=True)
    
    district_q = meta.Session.query(Districts)
    for info in reader:
        district = district_q.filter_by(
            district_type='City Council', state='NY',
            district_name='District %s' % info['district_id']).one()
        person = People()
        person.district_id = district.id
        person.fullname = info['fullname']
        district.people.append(person)
        # We don't want ID collisions between people from other systems
        # and TA's data, so as an ugly hack I'm adding a 'transalt.id'
        # metadata field so TA can identify their candidates.
        # If TA's app was using UUIDs, I could just use their IDs but
        # that's not happening now.
        status = PeopleMeta('candidate', True)
        person.meta.append(status)
        ta_id = PeopleMeta('transalt.id', info['nid'])
        person.meta.append(ta_id)

        meta.Session.save(person)
        meta.Session.save(status)
        meta.Session.save(ta_id)

    meta.Session.commit()

def downgrade():
    # Operations to reverse the above upgrade go here.

    from purplevoter.model import People, Districts, PeopleMeta, meta
    meta.metadata.bind = migrate_engine

    district_q = meta.Session.query(Districts)

    districts = district_q.filter_by(
            district_type='City Council', state='NY').all()
    for d in districts:
        for person in d.people:
            meta.Session.delete(person)

    meta.Session.commit()
    

    
