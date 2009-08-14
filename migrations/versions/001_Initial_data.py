from sqlalchemy import *
from migrate import *

# Converted from anil's mysql dump using... I forget which script.
# Yes, we are depending on PostGIS. No pretense at supporting other back ends.
import os.path

path = os.path.normpath(os.path.sep.join((os.path.dirname(__file__), 
                                          '001_Initial_data.pgsql')))
sql = open(path).read()

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
        connection.execute('DROP TABLE IF EXISTS districts CASCADE;')
        connection.execute('DROP TABLE IF EXISTS districts_meta CASCADE;')
        connection.execute('DROP TABLE IF EXISTS people CASCADE;')
        connection.execute('DROP TABLE IF EXISTS people_meta CASCADE;')
        connection.execute('DROP TABLE IF EXISTS elections CASCADE;')
        connection.execute('DROP TABLE IF EXISTS races CASCADE;')

        connection.execute('DROP SEQUENCE IF EXISTS districts_id_seq CASCADE;')
        connection.execute('DROP SEQUENCE IF EXISTS districts_meta_id_seq CASCADE;')
        connection.execute('DROP SEQUENCE IF EXISTS people_id_seq CASCADE;')
        connection.execute('DROP SEQUENCE IF EXISTS people_meta_id_seq CASCADE;')

        trans.commit()
    except:
        trans.rollback()
        raise
    pass
