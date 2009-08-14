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
    
    # district_type is often the same as contained people's 'office',
    # except in the case of districts like 'Brooklyn' or 'New York
    # City' that contain multiple offices.
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
    sa.Column("fullname", sa.types.String(255), nullable=False),
    sa.Column("incumbent_office", sa.types.String(255), nullable=True),
    sa.Column("incumbent_district", sa.types.Integer, sa.schema.ForeignKey('districts.id'),
              nullable=True),
    sa.Column("incumbent_district", sa.types.Integer, sa.schema.ForeignKey('districts.id'),
              nullable=True),
    sa.Column("race_id", sa.types.Integer, sa.schema.ForeignKey('races.id'), nullable=True),
    )

# Generic key-value pairs for annotating people.
people_meta_table = sa.Table("people_meta", meta.metadata,
    sa.Column("id", sa.types.Integer, primary_key=True),
    sa.Column("person_id", sa.types.Integer, sa.schema.ForeignKey("people.id")),
    sa.Column("meta_key", sa.types.String(255), nullable=False),
    sa.Column("meta_value", sa.types.UnicodeText, nullable=False),
    )

class People(object):
    '''represents a candidate or incumbent official.
    '''

    @property
    def election(self):
        # At some point we might care about historical elections,
        # and at that point we'll have to start caring about the
        # election dates to do anything useful.
        # For now, a person is associated w/ at most 1 election
        # and it's assumed to be "current".
        if not self.races:
            return None
        assert len(self.races) == 1
        return self.races[0].election

    @property
    def district(self):
        # See comment on self.election()
        if not self.races:
            return None
        assert len(self.races) == 1
        return self.races[0].district


class PeopleMeta(object):
    def __init__(self, key=None, val=None):
        if key is not None:
            self.meta_key = key
            self.meta_value = val


class Election(object):
    """represents an election with a date, which has any number of Races.
    """
#     @property
#     def districts(self):
#         return [r.district for r in self.races]

#     @property
#     def candidates(self):
#         return [r.candidates for r in self.races]



# Allowed stages for elections are based on things I've found in the Votesmart data.
# Are we missing any?
# Congressional special elections are just called 'General' by VS.
# Same for the california recall election of 2003.
election_stages = ('General', 'Primary', 'General Runoff', 'Primary Runoff')

election_table = sa.Table(
    "elections", meta.metadata,
    sa.Column("id", sa.types.Integer, primary_key=True),
    sa.Column("name", sa.types.Unicode(255), nullable=False),
    sa.Column("date", sa.types.Date(), nullable=False),
    sa.Column("stagename", sa.types.String(127),
              sa.schema.CheckConstraint("stagename IN %s" % str(election_stages),
                                        name='stagename_values_constraint'),
              nullable=False,
              ),
    sa.UniqueConstraint('name', 'date', 'stagename', name='election_uniqueness_constr'),
    )


class Race(object):
    """Models a unique trio of (Election, District, 'Office name').
    """
    def __init__(self, election, district, office, candidates=None):
        self.election = election
        self.district = district
        self.office = office
        if candidates:
            self.candidates = candidates

race_table = sa.Table(
    'races', meta.metadata,
    sa.Column("id", sa.types.Integer, primary_key=True),
    sa.Column('election_id', sa.types.Integer, 
              sa.schema.ForeignKey('elections.id'), nullable=False,
              ),
    sa.Column('district_id', sa.types.Integer, 
              sa.schema.ForeignKey('districts.id'), nullable=False,
              ),
    sa.Column('office', sa.types.Unicode(255), nullable=False,
              ),
    )



orm.mapper(Race, race_table,
           properties={'district': orm.relation(Districts,
                                                backref='races',
                                                ),
                       'election': orm.relation(Election,
                                                backref='races',
                                                ),
                       'candidates': orm.relation(People,
                                                  backref='races',
                                                  ),
                       })
       

orm.mapper(Districts, districts_table,
           properties={# Don't use cascade here, I think that we don't want
                       # want people to be deleted even if their district is
                       # deleted. Not sure.
                       'incumbents': orm.relation(People),
                       })

orm.mapper(People, people_table,
           properties={'meta': orm.relation(PeopleMeta, 
                                            backref='person', 
                                            cascade="all, delete, delete-orphan"),
                       })

orm.mapper(PeopleMeta, people_meta_table)

orm.mapper(Election, election_table)
