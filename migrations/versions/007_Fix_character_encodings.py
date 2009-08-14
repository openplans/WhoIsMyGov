from sqlalchemy import *
import sqlalchemy as sa
from migrate import *

def upgrade():
    # Our data got double-encoded somehow.
    # This fixes it to be proper utf8.
    from purplevoter.model import People, meta
    meta.metadata.bind = migrate_engine
    people = meta.Session.query(People).all()
    for p in people:
        try:
            fullname = p.fullname.decode('utf8').encode('latin1').decode('utf8')
        except UnicodeDecodeError:
            print "couldn't fix %s, skipping" % fullname
            continue
        if fullname != p.fullname:
            print "Fixed", fullname.encode('utf8')
            p.fullname = fullname
    meta.Session.commit()

def downgrade():
    # Operations to reverse the above upgrade go here.

    # Redefine the models (and a new MetaData instance) to avoid
    # caring what version of code we have.
    from sqlalchemy.orm import scoped_session, sessionmaker
    Session = scoped_session(sessionmaker())
    from sqlalchemy import MetaData
    metadata = MetaData()

    metadata.bind = migrate_engine
    people_table = sa.schema.Table('people', metadata, autoload=True)
    class People(object):
        pass
    sa.orm.mapper(People, people_table)
    people = Session.query(People).all()
    for p in people:
        # Re-mangle the data??
        try:
            fullname = p.fullname.encode('utf8').decode('latin1').encode('utf8')
            if p.fullname != fullname:
                p.fullname = fullname
        except UnicodeDecodeError:
            print "couldn't mangle %s, skipping" % fullname
    Session.commit()

