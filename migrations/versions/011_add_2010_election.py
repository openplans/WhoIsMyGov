from sqlalchemy import *
from migrate import *
import sqlalchemy

import os.path
import datetime

from migrations.utils import find_or_create
from migrations.utils import CaseNormalizingDictReader

ELECTION_NAME = u'New York State 2010'
ELECTION_STAGE = u'General'
    
def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.
    from whoismygov.model import meta, Election, Districts
    meta.metadata.bind = migrate_engine
    connection = migrate_engine.connect()

    # Add NYS shapefile.
    # Fun with polygons, geojson, and shapely.
    import geojson
    import shapely
    here = os.path.abspath(__file__)
    nys_file = os.path.normpath(os.path.join(
            here, '../../../misc_import_data/ny_state/st36_d00.json'))
    nys_json = geojson.load(open(nys_file))
    nys_polygons = None
    for feature in nys_json['features']:
        poly = shapely.geometry.asShape(feature['geometry'])
        if nys_polygons is None:
            nys_polygons = poly
        else:
            nys_polygons = nys_polygons.union(poly)

    nys = find_or_create(meta.Session, Districts,
                         state=u'NY',
                         district_type=u'State',
                         level_name=u'State',
                         district_name=u'New York State',
                         parent_id=None,
                         geometry=nys_polygons,
                         )

    # Have to commit now in order to get an ID. Argh.
    meta.Session.commit()

    # Every district in NYS without a parent district is a child of NYS.
    connection.execute("UPDATE districts SET parent_id = %s " 
                       " WHERE state = 'NY' AND parent_id = NULL" % nys.id)

    election = find_or_create(meta.Session, Election,
                              date=datetime.date(2010, 11, 2),
                              name=ELECTION_NAME,
                              stagename=ELECTION_STAGE)


    files = [dict(path='batch_01_20100818_1452.csv')]

    for params in files:
        _insert_from_file(engine=migrate_engine, election=election,
                          **params)

    # TODO: NYS Senate and NYS Assembly have no geometries!


def _insert_from_file(path, election, engine):

    from whoismygov.model import People, Districts, PeopleMeta, meta, Race
    meta.metadata.bind = engine

    path = os.path.join(os.path.dirname(__file__),
                        '..', '..', 'misc_import_data',
                        'ta_candidate_info_20100818', path
                        )
    csv_path = os.path.normpath(path)
    reader = CaseNormalizingDictReader(open(csv_path, 'r'), skipinitialspace=True)
    district_q = meta.Session.query(Districts)

    for info in reader:
        district_type = office = unicode(info['office'])
        if office == 'Governor':
            district_name = u'New York State'
            district_type = u'State'
        else:
            district_name = u'District %s' % info['districtnumber']

        district = district_q.filter_by(
            district_type=district_type, state='NY',
            district_name=district_name).one()

        race = find_or_create(meta.Session, Race,
                              election=election, district=district,
                              office=office)

        fullname = info['name']
        fullname = ' '.join(fullname.split()).title()
        person = find_or_create(meta.Session, People, fullname=fullname)

        race.candidates.append(person)

        # We don't want ID collisions between people from other systems
        # and TA's data, so as an ugly hack I'm adding a 'transaltid'
        # metadata field so TA can identify their candidates.
        # If TA's app was using UUIDs, I could just use their IDs but
        # that's not happening now.

        transaltid = (info.get('transaltid') or '').strip()
        if transaltid:
            ta_id = find_or_create(meta.Session, PeopleMeta,
                                   meta_key=u'transaltid', 
                                   meta_value=unicode(transaltid),
                                   person=person)

        print u"Added", person.fullname


    meta.Session.commit()

def downgrade():
    # Operations to reverse the above upgrade go here.
    from whoismygov.model import meta
    meta.metadata.bind = migrate_engine
    connection = migrate_engine.connect()

    # Delete people who are in 2010 races.
    # First their metadata...
    connection.execute(
        "DELETE FROM people_meta WHERE person_id IN "
        " (SELECT id FROM people WHERE race_id IN "
        "  (SELECT id FROM races WHERE election_id IN "
        "   (SELECT id FROM elections WHERE name = '%s' AND stagename = '%s')));"
        % (ELECTION_NAME, ELECTION_STAGE))

    # Now the people...
    connection.execute(
        "DELETE FROM people WHERE race_id IN "
        " (SELECT id FROM races WHERE election_id IN "
        "  (SELECT id FROM elections WHERE name = '%s' AND stagename = '%s'));"
        % (ELECTION_NAME, ELECTION_STAGE))
    
    # And delete the relevant races...
    connection.execute(
        "DELETE FROM races WHERE races.election_id IN "
        " (SELECT id FROM elections WHERE name = '%s' AND stagename = '%s');"
        % (ELECTION_NAME, ELECTION_STAGE))

    # And the election we added.
    connection.execute("DELETE FROM elections WHERE elections.name = '%s'"
                       " AND elections.stagename = '%s';" % 
                       (ELECTION_NAME, ELECTION_STAGE))

    # And NYS.
    connection.execute("UPDATE districts SET parent_id = NULL " 
                       " WHERE state = 'NY' AND parent_id IN "
                       "  (SELECT id FROM districts WHERE district_name ="
                       "   'New York State');")
    connection.execute(
        "DELETE FROM districts WHERE district_name = 'New York State'")
    
    meta.Session.commit()
