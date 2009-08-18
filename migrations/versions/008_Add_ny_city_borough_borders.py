from sqlalchemy import *
from migrate import *

meta = MetaData(migrate_engine)

import os.path

def upgrade():
    here = os.path.abspath(__file__)
    borough_shapes = os.path.normpath(os.path.join(
            here, '../../../misc_import_data/ny_boroughs/nybb.sql'))
    sql = open(borough_shapes).read()
    connection = migrate_engine.connect()
    trans = connection.begin()
    from purplevoter.model.meta import storage_SRID
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
        connection.execute(sql)
        connection.execute('update districts set geometry=(ST_TRANSFORM(geometry, %r)) where geometry is not null;' % storage_SRID)
        # Now put the constraint back!!
        connection.execute('ALTER TABLE districts ADD CONSTRAINT "enforce_srid_geometry" CHECK (SRID(geometry)=%s);' % storage_SRID)

        # Generate a shape for all of NYC by taking the union of the boroughs.
        connection.execute("INSERT INTO districts (state, district_type, level_name, district_name, geometry) SELECT 'NY', 'City', 'City', 'New York City', ST_Union(geometry) from districts where state = 'NY' and level_name = 'City' and (district_type = 'Borough'  or district_type = 'City Council');")
        trans.commit()
    except:
        trans.rollback()
        raise

def downgrade():
    # Operations to reverse the above upgrade go here.
    connection = migrate_engine.connect()
    try:
        connection.execute("DELETE FROM districts WHERE state = 'NY' and (district_type = 'Borough' or district_type = 'City');")
    except:
        pass
