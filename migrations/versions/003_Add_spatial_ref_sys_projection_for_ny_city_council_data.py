"""
Migration needed before we can import the NY City Council data.
"""

from sqlalchemy import *
from migrate import *
from sqlalchemy.ext.sqlsoup import SqlSoup

# This may or may not be functionally identical to SRID 2831?  Not
# taking chances, since I don't know how to tell if the slight difference in
# proj4text matters, I'm going to use this.

# Got this from http://spatialreference.org/ref/esri/102718/
sql = 'INSERT into spatial_ref_sys (srid, auth_name, auth_srid, proj4text, srtext) values ( 9102718, \'esri\', 102718, \'+proj=lcc +lat_1=40.66666666666666 +lat_2=41.03333333333333 +lat_0=40.16666666666666 +lon_0=-74 +x_0=300000 +y_0=0 +ellps=GRS80 +datum=NAD83 +to_meter=0.3048006096012192 +no_defs \', \'PROJCS[\"NAD_1983_StatePlane_New_York_Long_Island_FIPS_3104_Feet",GEOGCS["GCS_North_American_1983",DATUM["North_American_Datum_1983",SPHEROID["GRS_1980",6378137,298.257222101]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]],PROJECTION["Lambert_Conformal_Conic_2SP"],PARAMETER["False_Easting",984249.9999999999],PARAMETER["False_Northing",0],PARAMETER["Central_Meridian",-74],PARAMETER["Standard_Parallel_1",40.66666666666666],PARAMETER["Standard_Parallel_2",41.03333333333333],PARAMETER["Latitude_Of_Origin",40.16666666666666],UNIT["Foot_US",0.30480060960121924],AUTHORITY["EPSG","102718"]]\');'

meta = MetaData(migrate_engine)

def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.
    connection = migrate_engine.connect()
    trans = connection.begin()
    try:
        connection.execute(sql)
        trans.commit()
    except:
        trans.rollback()
        raise


def downgrade():
    # Operations to reverse the above upgrade go here.
    connection = migrate_engine.connect()
    trans = connection.begin()
    try:
        connection.execute('delete from spatial_ref_sys where srid = 9102718;')
        trans.commit()
    except:
        trans.rollback()
        raise
    pass
