from purplevoter.tests import *

class TestPeopleController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='people', action='index'))
        # Test response...
