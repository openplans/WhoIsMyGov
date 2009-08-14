from sqlalchemy import *
from migrate import *
import migrate.changeset

meta = MetaData(migrate_engine)

def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.
    return


def downgrade():
    # Operations to reverse the above upgrade go here.
    return

