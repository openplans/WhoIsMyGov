from sqlalchemy import *
from migrate import *
import sqlalchemy

import os.path
import csv
import datetime
        
    
def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.
    from purplevoter.model import meta, Election
    meta.metadata.bind = migrate_engine
    connection = migrate_engine.connect()

    election_q = meta.Session.query(Election)
    try:
        election = election_q.filter_by(date=datetime.date(2009, 8, 15),
                                        name='New York City 2009',
                                        stagename='Primary').one()
    except sqlalchemy.orm.exc.NoResultFound:
        election = Election(date=datetime.date(2009, 9, 15),
                            name='New York City 2009',
                            stagename='Primary')
        meta.Session.save(election)

    raise ValueError('I gotta stop here or i will die')

    files = (('City Council', 'City Council', r'District %s', 'Election_Survey_city_council_20090811.csv'),
             ('Mayor', 'City', 'New York City', 'Election_Survey_mayoral_20090811.csv'),
             )
    for office, district_type, district_format, path in files:
        _insert_from_file(office=office, 
                          district_type=district_type, 
                          district_format=district_format, 
                          path=path, election=election,
                          engine=migrate_engine)

def _insert_from_file(office, district_type, district_format, path, election, engine):
    from purplevoter.model import People, Districts, PeopleMeta, meta, Race
    meta.metadata.bind = engine

    csv_path = os.path.join(os.path.dirname(__file__), path)
    reader = csv.DictReader(open(csv_path, 'r'), skipinitialspace=True)

    district_q = meta.Session.query(Districts)
    race_q = meta.Session.query(Race)

    for info in reader:
        if district_format.count('%'):
            district_name = district_format % info['Council District'] #XXX or what?
        else:
            district_name = district_format

        district = district_q.filter_by(
            district_type=district_type, state='NY',
            district_name=district_name).one()

        try:
            race = race_q.filter_by(election=election, district=district, office=office).one()
        except: # XXX
            race = Race(election, district, office)
            meta.Session.save(race)

        try:
            person = person_q.filter_by(fullname=info['Name']).one()
        except:
            person = People()
            person.fullname = info['Name']
            meta.Session.save(person)

        race.candidates.append(person)

        # We don't want ID collisions between people from other systems
        # and TA's data, so as an ugly hack I'm adding a 'transalt.id'
        # metadata field so TA can identify their candidates.
        # If TA's app was using UUIDs, I could just use their IDs but
        # that's not happening now.

        ta_id = PeopleMeta('transalt_id', info['NID'])
        person.meta.append(ta_id)

        meta.Session.save(ta_id)

        print u"Added", person.fullname

    meta.Session.commit()

def downgrade():
    # Operations to reverse the above upgrade go here.
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.
    from purplevoter.model import meta, Election
    meta.metadata.bind = migrate_engine
    connection = migrate_engine.connect()

    connection.execute("UPDATE people_meta SET meta_key = 'transalt.id' WHERE meta_key = 'transaltid';")

    try:
        connection.execute('ALTER TABLE people RENAME COLUMN incumbent_district TO district_id;')
    except:
        pass

    try:
        connection.execute('ALTER TABLE people DROP COLUMN race_id;')
    except:
        pass

    try:
        connection.execute('TRUNCATE TABLE races;')
        connection.execute('ALTER TABLE races DROP CONSTRAINT races_district_id_key;')
        connection.execute('TRUNCATE TABLE races DROP CONSTRAINT races_election_id_key;')
    except:
        pass

    try:
        connection.execute("DELETE FROM elections WHERE election.name = 'New York City 2009'"
                           " AND election.stagename = 'Primary';")
    except:
        pass

