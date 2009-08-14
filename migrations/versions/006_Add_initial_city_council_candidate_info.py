from sqlalchemy import *
from migrate import *

import os.path
import csv

def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.

    try:
        connection.execute('ALTER TABLE people RENAME COLUMN district_id TO incumbent_district;')
    except:
        # might already have that in the DB?
        pass

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
        try:
            person.district_id = district.id
        except AttributeError:
            person.incumbent_district = district_id
        person.fullname = info['fullname']
        try:
            district.people.append(person)
        except AttributeError:
            # we might have a version of the app that doesn't have District.people??
            pass
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
    from purplevoter.model import meta

    meta.metadata.bind = migrate_engine

    connection = migrate_engine.connect()
    sql = "DELETE FROM people AS p WHERE p.id IN (SELECT d.id FROM districts AS d WHERE d.district_type = 'City Council' AND d.state = 'NY');"
    migrate_engine.execute(sql)
    

    
