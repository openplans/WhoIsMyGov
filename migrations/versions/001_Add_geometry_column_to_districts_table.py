from sqlalchemy import *
from migrate import *
import migrate.changeset

meta = MetaData(migrate_engine)
storage_SRID = 4326

def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.
    table = Table('districts', meta, autoload=True)
    # kinda have to violate the "don't import stuff from your app" edict here...
    # sqlgeotypes should get factored out from the app anyway.
    from purplevoter.model.sqlgeotypes import Geometry
    col = Column("geometry", Geometry(storage_SRID, 'GEOMETRY', 2), nullable=True)
    col.create(table)
    assert col is table.columns.geometry

def downgrade():
    # Operations to reverse the above upgrade go here.
    table = Table('districts', meta, autoload=True)
    col = table.columns.geometry
    col.drop()

