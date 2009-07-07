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

# Generic key-value pairs for annotating districts.
districts_meta_table = sa.Table("districts_meta", meta.metadata,
    sa.Column("id", sa.types.Integer, primary_key=True),
    sa.Column("district_id", sa.types.Integer, sa.schema.ForeignKey("districts.id")),
    sa.Column("meta_key", sa.types.String(255), nullable=False),
    sa.Column("meta_value", sa.types.UnicodeText, nullable=False)
    )

class DistrictsMeta(object):
    pass

orm.mapper(Districts, districts_table, 
           properties={'meta': orm.relation(DistrictsMeta, 
                                            backref='district', 
                                            cascade="all, delete, delete-orphan"),})

orm.mapper(DistrictsMeta, districts_meta_table)
