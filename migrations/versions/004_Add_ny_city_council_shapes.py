from sqlalchemy import *
from migrate import *

meta = MetaData(migrate_engine)

import os.path

def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.
    here = os.path.abspath(__file__)
    district_shapes = os.path.normpath(os.path.join(
            here, '../../../misc_import_data/ny_city_council_districts/nycc.sql'))
    main_sql = open(district_shapes).read()
    connection = migrate_engine.connect()
    trans = connection.begin()
    from whoismygov.model.meta import storage_SRID
    try:
        # I can't get shp2pgsql to convert the SRID, which means I
        # have to temporarily allow putting in data with a bad SRID,
        # then convert the data in-place. Stupid but effective.
        try:
            connection.execute('ALTER TABLE districts DROP CONSTRAINT "enforce_srid_geometry" RESTRICT;')
        except:  # XXX what exeption?  
            # Sometimes the constraint doesn't exist yet when this
            # migration runs?  That's OK.
            trans.rollback()
            trans = connection.begin()
        connection.execute(main_sql)
        connection.execute('update districts set geometry=(ST_TRANSFORM(geometry, %r)) where geometry is not null;' % storage_SRID)
        # Now put the constraint back!!
        connection.execute('ALTER TABLE districts ADD CONSTRAINT "enforce_srid_geometry" CHECK (SRID(geometry)=%s);' % storage_SRID)
        trans.commit()
    except:
        trans.rollback()
        raise
        

def downgrade():
    # Operations to reverse the above upgrade go here.
    connection = migrate_engine.connect()
    trans = connection.begin()
    try:
        connection.execute("DELETE from districts where state = 'NY' and district_type = 'City Council' and level_name = 'City';")
        trans.commit()
    except:
        trans.rollback()
        raise
