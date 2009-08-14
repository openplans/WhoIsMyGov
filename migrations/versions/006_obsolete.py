from sqlalchemy import *
from migrate import *

def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.
    
    # There used to be something here, but it became irrelevant.
    return


def downgrade():
    # Operations to reverse the above upgrade go here.
    pass
    
