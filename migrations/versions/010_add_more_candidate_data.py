from sqlalchemy import *
from migrate import *
import sqlalchemy

import os.path
import csv
import datetime

def find_or_create(session, model, **kw):
    # Rails has something like this, too bad SA doesn't.
    query = session.query(model)
    try:
        instance = query.filter_by(**kw).one()
    except sqlalchemy.orm.exc.NoResultFound:
        instance = model(**kw)
        session.save(instance)
    return instance

    
def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.
    from purplevoter.model import meta, Election
    meta.metadata.bind = migrate_engine
    connection = migrate_engine.connect()

    election = find_or_create(meta.Session, Election,
                              date=datetime.date(2009, 9, 15),
                              name='New York City 2009',
                              stagename='Primary')

    files = [dict(path='city_council.csv', office='City Council',
                  district_type='City Council', district_format=r'District %s'),
             dict(path='mayoral.csv', office='Mayor', 
                  district_type='City', district_format='New York City'),
             dict(path='comptroller.csv', office='Comptroller',
                  district_type='City', district_format='New York City'),
             dict(path='district_attorney.csv', office='District Attorney',
                  district_type='Borough', district_format=r'%s'),
             dict(path='public_advocate.csv', office='Public Advocate',
                  district_type='City', district_format='New York City'),
             ]

    for params in files:
        _insert_from_file(engine=migrate_engine, election=election,
                          **params)


def _insert_from_file(office, district_type, district_format, path, 
                      election, engine):
    from purplevoter.model import People, Districts, PeopleMeta, meta, Race
    meta.metadata.bind = engine

    path = os.path.join(os.path.dirname(__file__),
                        '..', '..', 'misc_import_data', 
                        'ta_candidate_info_20090813',
                        path
                        )
    csv_path = os.path.normpath(path)
    reader = csv.DictReader(open(csv_path, 'r'), skipinitialspace=True)

    district_q = meta.Session.query(Districts)

    for info in reader:
        if district_type == 'City Council' and district_format.count:
            district_name = district_format % info['Council District']
        elif district_type == 'Borough':
            district_name = info['borough']
        else:
            district_name = district_format

        district = district_q.filter_by(
            district_type=district_type, state='NY',
            district_name=district_name).one()

        race = find_or_create(meta.Session, Race,
                              election=election, district=district,
                              office=office)
        person = find_or_create(meta.Session, People, fullname=info['fullname'])

        race.candidates.append(person)

        # We don't want ID collisions between people from other systems
        # and TA's data, so as an ugly hack I'm adding a 'transaltid'
        # metadata field so TA can identify their candidates.
        # If TA's app was using UUIDs, I could just use their IDs but
        # that's not happening now.

        transaltid = info.get('NID', '').strip()
        if transaltid:
            ta_id = find_or_create(meta.Session, PeopleMeta,
                                   meta_key='transaltid', meta_value=transaltid,
                                   person=person)

        print u"Added", person.fullname

    meta.Session.commit()

def downgrade():
    # Operations to reverse the above upgrade go here.
    from purplevoter.model import meta
    meta.metadata.bind = migrate_engine
    connection = migrate_engine.connect()

    # This was the first time we inserted any races, so we just delete
    # all those people.
    connection.execute('DELETE FROM people_meta WHERE people_meta.person_id IN (SELECT people.id FROM people INNER JOIN races ON people.race_id = races.id);')
    connection.execute('DELETE FROM people WHERE people.id IN (SELECT people.id FROM people INNER JOIN races ON people.race_id = races.id);')

    # And delete all the races...
    connection.execute('DELETE FROM races;')

    # And the election we added.
    connection.execute("DELETE FROM elections WHERE elections.name = 'New York City 2009'"
                       " AND elections.stagename = 'Primary';")

    meta.Session.commit()
