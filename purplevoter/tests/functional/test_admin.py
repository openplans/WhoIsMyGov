from purplevoter.tests import *

class TestAdminController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='admin', action='index'))
        # Test response...
