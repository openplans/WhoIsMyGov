"""The application's model objects"""

from whoismygov.model import meta
from sqlalchemy import orm
from sqlalchemy.orm.exc import NoResultFound
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
    
    # district_type is often the same as a related race's 'office',
    # except in the case of districts like 'Brooklyn' or 'New York
    # State' that contain multiple offices.
    sa.Column("district_type", sa.types.String(255), nullable=False),
    sa.Column("level_name", sa.types.String(255), nullable=False),
    sa.Column("district_name", sa.types.String(255), nullable=False),
    sa.Column("parent_id", sa.schema.ForeignKey('districts.id',
                                                ondelete='SET DEFAULT'),
              nullable=True),

    # Districts that have a NULL geometry just won't show up in
    # searches.  That's OK, we typically use external APIs (eg
    # mobilecommons) for those, and just have the district in our DB as
    # a stub.
    sa.Column("geometry", Geometry(meta.storage_SRID, 'GEOMETRY', 2), nullable=True),
    )

class Districts(object):

    @property
    def parent_district(self):
        """occasionally it's useful to know a geographic district that
        encompasses this one, eg. in New York, a City Council district
        is part of a certain Borough.
        """
        # Tried to do this via an orm.relation but I couldn't figure out
        # how to get it to work the right way with a self-join.
        if self.parent_id is None:
            return None
        q = meta.Session.query(Districts)
        try:
            parent = q.filter_by(id=self.parent_id).one()
            return parent
        except NoResultFound:
            return None

    @property
    def parent_district_name(self):
        parent = self.parent_district
        if parent:
            return parent.district_name
        return None
            


people_table = sa.Table(
    "people", meta.metadata,
    sa.Column("id", sa.types.Integer, primary_key=True, autoincrement=True),
    sa.Column("fullname", sa.types.String(255), nullable=False),
    sa.Column("incumbent_office", sa.types.String(255), nullable=True),
    sa.Column("incumbent_district", sa.types.Integer, 
              sa.schema.ForeignKey('districts.id', ondelete='SET DEFAULT'),
              nullable=True),
    sa.Column("race_id", sa.types.Integer, sa.schema.ForeignKey('races.id'), nullable=True),
    )

# Generic key-value pairs for annotating people.
people_meta_table = sa.Table("people_meta", meta.metadata,
    sa.Column("id", sa.types.Integer, primary_key=True),
    sa.Column("person_id", sa.types.Integer, sa.schema.ForeignKey("people.id"),
              nullable=False),
    sa.Column("meta_key", sa.types.String(255), nullable=False),
    sa.Column("meta_value", sa.types.UnicodeText, nullable=False),
    )

class People(object):
    '''represents a candidate or incumbent official.
    '''

    def __init__(self, fullname=None, incumbent_office=None,
                 incumbent_district=None):
        if fullname:
            self.fullname=fullname
        if incumbent_office:
            self.incumbent_office=incumbent_office
        if incumbent_district:
            self.incumbent_district=incumbent_district

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
    def __init__(self, person, meta_key, meta_value):
        self.person = person
        self.meta_key = meta_key
        self.meta_value = meta_value


class Election(object):
    """represents an election with a date, which has any number of Races.
    """
    def __init__(self, date, name, stagename):
        self.date = date
        self.name = name
        self.stagename = stagename

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

    @property
    def incumbents(self):
        # should figure out a way to get sqlalchemy to do this.
        # raw sql?
        return [i for i in self.district.incumbents if i.incumbent_office == self.office]


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
       

orm.mapper(
    Districts, districts_table,
    properties={# Don't use cascade here, I think that we don't want
                # want people to be deleted even if their district is
                # deleted. Not sure.
                'incumbents': orm.relation(People, backref='incumbent_district_obj'),
                })

orm.mapper(People, people_table,
           properties={'meta': orm.relation(PeopleMeta, 
                                            backref='person', 
                                            cascade="all, delete, delete-orphan"),
                       })

orm.mapper(PeopleMeta, people_meta_table)

orm.mapper(Election, election_table)
