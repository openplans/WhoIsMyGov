"""The application's model objects"""

from purplevoter.model import meta
from sqlalchemy import orm
from sqlgeotypes import Geometry
import sqlalchemy as sa

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    meta.Session.configure(bind=engine)
    meta.engine = engine

districts_table = sa.Table(
    "districts", meta.metadata,
    sa.Column("id", sa.types.Integer, primary_key=True),
    sa.Column("state", sa.types.String(255), nullable=False),
    sa.Column("district_type", sa.types.String(255), nullable=False),
    sa.Column("level_name", sa.types.String(255), nullable=False),
    sa.Column("district_name", sa.types.String(255), nullable=False),
    sa.Column("geometry", Geometry(meta.storage_SRID, 'GEOMETRY', 2), nullable=True),
    )

class Districts(object):
    pass


people_table = sa.Table(
    "people", meta.metadata,
    sa.Column("id", sa.types.Integer, primary_key=True),
    sa.Column("district_id", sa.types.Integer, sa.schema.ForeignKey("districts.id")),
    sa.Column("fullname", sa.types.String(255), nullable=False),
    )

# Generic key-value pairs for annotating people.
people_meta_table = sa.Table("people_meta", meta.metadata,
    sa.Column("id", sa.types.Integer, primary_key=True),
    sa.Column("person_id", sa.types.Integer, sa.schema.ForeignKey("people.id")),
    sa.Column("meta_key", sa.types.String(255), nullable=False),
    sa.Column("meta_value", sa.types.UnicodeText, nullable=False)
    )

class People(object):
    pass

class PeopleMeta(object):
    def __init__(self, key=None, val=None):
        if key is not None:
            self.meta_key = key
            self.meta_value = val


orm.mapper(Districts, districts_table,
           properties={'people': orm.relation(People,
                                              backref='district',
                                              cascade='all, delete, delete-orphan'),})

orm.mapper(People, people_table,
           properties={'meta': orm.relation(PeopleMeta, 
                                            backref='person', 
                                            cascade="all, delete, delete-orphan"),})

orm.mapper(PeopleMeta, people_meta_table)
