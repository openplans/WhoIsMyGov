from purplevoter.tests import *

class TestPeopleController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='people', action='index'))
        # Test response...

    def test_geocoder(self):
        response = self.app.get(url(controller='people', action='search', address='669 degraw st, 11217'))
        # senate
        assert 'Charles Schumer' in response
        assert 'Kirsten Gillibrand' in response

        # fed rep - D 11
        assert 'Yvette D. Clarke' in response

        # city council
        assert 'David Yassky' in response

        # state assembly - D 52
        assert 'Joan Millman' in response

        # state senate - D 18
        assert 'Velmanette Montgomery' in response
