"""SQLAlchemy Metadata and Session object"""
from sqlalchemy import MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

__all__ = ['Session', 'engine', 'metadata']

# SQLAlchemy database engine. Updated by model.init_model()
engine = None

# SQLAlchemy session manager. Updated by model.init_model()
Session = scoped_session(sessionmaker())

# Global metadata. If you have multiple databases with overlapping table
# names, you'll need a metadata for each database
metadata = MetaData()

# 4326 is the SRID for WGS84
# (http://en.wikipedia.org/wiki/World_Geodetic_System) ... which seems
# to be what blockparty uses; stores things as lon/lat internally.
# Since the main thing we want to query is whether a lon,lat point is
# within a given district, and we don't care much about distances and
# suchlike, this is a good choice.
storage_SRID = 4326
