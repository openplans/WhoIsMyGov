from sqlalchemy import *
from migrate import *

meta = MetaData(migrate_engine)

# Populate the 'office' attribute on candidates.
# This is a bit denormalized, but better than stuffing this data into
# the generic people_meta table.
up_sql = """
UPDATE people SET incumbent_office=(
 SELECT districts.district_type FROM districts
  WHERE districts.id = people.incumbent_district)
;
"""

def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.
    connection = migrate_engine.connect()
    trans = connection.begin()
    try:
        try:
            connection.execute('ALTER TABLE people ADD COLUMN "incumbent_office" varchar(255);')
        except:
            trans.rollback()
            trans = connection.begin()
        connection.execute(up_sql)
        trans.commit()
    except:
        trans.rollback()
        raise


down_sql = """
UPDATE districts SET district_type=(
 SELECT people.incumbent_office FROM people
  WHERE districts.id = people.district_id
  AND people.incumbent_office IS NOT NULL)
;
"""
def downgrade():
    # Operations to reverse the above upgrade go here.
    connection = migrate_engine.connect()
    trans = connection.begin()
    try:
        connection.execute(down_sql)
        trans.commit()
    except:
        trans.rollback()
        pass
    pass
