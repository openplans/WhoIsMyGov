from sqlalchemy import *
from migrate import *

from sqlalchemy.ext.sqlsoup import SqlSoup
meta = MetaData(migrate_engine)

import os.path

def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.
    db = SqlSoup(migrate_engine)
    here = os.path.abspath(__file__)
    district_shapes = os.path.normpath(os.path.join(
            here, '../../../misc_import_data/ny_city_council_districts/nycc.sql'))
    sql = open(district_shapes).read()
    db.bind.execute(sql)

def downgrade():
    # Operations to reverse the above upgrade go here.
    db = SqlSoup(migrate_engine)
    db.bind.execute("DELETE from districts where state = 'NY' and district_type = 'City Council' and level_name = 'City';")

