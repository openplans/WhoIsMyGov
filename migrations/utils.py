"""Stuff useful for multiple migrations
"""

import csv

def find_or_create(session, model, **kw):
    import sqlalchemy
    # Rails has something like this, too bad SA doesn't.
    query = session.query(model)
    try:
        instance = query.filter_by(**kw).one()
    except sqlalchemy.orm.exc.NoResultFound:
        try:
            instance = model(**kw)
        except TypeError:
            # Not sure why some are not usable as args to __init__()
            instance = model()
            for key, val in kw.items():
                setattr(instance, key, val)

        session.save(instance)
    return instance


class CaseNormalizingDictReader(csv.DictReader):

    # I wish DictReader had an option for case-insensitive keys.
    # So here it is.

    class CaseNormalizingDict(dict):

        def __getitem__(self, key):
            # hacking __setitem__ would probably be smarter. eh.
            for k in key, key.lower(), key.upper(), key.title():
                try:
                    return dict.__getitem__(self, k)
                except KeyError:
                    continue
            raise KeyError(key)

        def get(self, key, default=None):
            try:
                return self[key]
            except KeyError:
                return default

    def next(self):
        d = csv.DictReader.next(self)
        return self.CaseNormalizingDict(d)
