from sqlalchemy import *
from migrate import *
import migrate.changeset

meta = MetaData(migrate_engine)

def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.
    from purplevoter.model.meta import storage_SRID
    sql = "SELECT AddGeometryColumn('districts','geometry', %r, 'GEOMETRY', 2);" 
    sql = sql % storage_SRID
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
    table = Table('districts', meta, autoload=True)
    col = table.columns.geometry
    col.drop()

