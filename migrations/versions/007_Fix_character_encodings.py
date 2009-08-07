from sqlalchemy import *
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
    from purplevoter.model import People, meta
    meta.metadata.bind = migrate_engine
    people = meta.Session.query(People).all()
    for p in people:
        # Re-mangle the data??
        try:
            fullname = p.fullname.encode('utf8').decode('latin1').encode('utf8')
            if p.fullname != fullname:
                p.fullname = fullname
        except UnicodeDecodeError:
            print "couldn't mangle %s, skipping" % fullname
    meta.Session.commit()

