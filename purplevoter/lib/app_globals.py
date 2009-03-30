"""The application's Globals object"""

class Globals(object):

    """Globals acts as a container for objects available throughout the
    life of the application

    """

    def __init__(self):
        """One instance of Globals is created during application
        initialization and is available during requests via the
        'app_globals' variable

        """
        self.google_api_key = 'ABQIAAAATLgg7qN2CAG1jao7NPt9ChQChx54JYdgbPKio935j7RDK0bGdhSD0vfkVZsJyvz33c8aJO_vRikkuQ'
