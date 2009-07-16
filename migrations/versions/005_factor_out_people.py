from sqlalchemy import *
from migrate import *

meta = MetaData(migrate_engine)

up_sql = """
INSERT INTO people (fullname, district_id)
 SELECT meta_value, district_id
   FROM districts_meta
    WHERE meta_key in ('official', 'Official');

DELETE FROM districts_meta WHERE meta_key in ('official', 'Official');
"""


down_sql = """
INSERT INTO districts_meta (district_id, meta_key, meta_value)
 SELECT district_id, 'official', fullname FROM people;

TRUNCATE TABLE people CASCADE;
"""

def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.
    connection = migrate_engine.connect()
    trans = connection.begin()
    try:
        connection.execute(up_sql)
        trans.commit()
    except:
        trans.rollback()
        raise
        

def downgrade():
    # Operations to reverse the above upgrade go here.
    connection = migrate_engine.connect()
    trans = connection.begin()
    try:
        connection.execute(down_sql)
        trans.commit()
    except:
        trans.rollback()
        raise
