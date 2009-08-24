from purplevoter.tests import url, TestController

class TestPeopleController(TestController):

    degraw = '669 degraw st., 11217'

#     def test_geocoder_senate(self):
#         response = self.app.get(url(controller='people', action='search', address=self.degraw))

#         assert 'Charles Schumer' in response
#         assert 'Kirsten Gillibrand' in response

#     def test_geocoder_us_house(self):
#         response = self.app.get(url(controller='people', action='search', address=self.degraw))
#         # fed rep - D 11
#         assert 'Yvette D. Clarke' in response

#     def test_geocoder_state_assembly(self):
#         response = self.app.get(url(controller='people', action='search', address=self.degraw))
#         # state assembly - D 52
#         assert 'Joan Millman' in response

#     def test_geocoder_state_senate(self):
#         response = self.app.get(url(controller='people', action='search', address=self.degraw))
#         # state senate - D 18
#         assert 'Velmanette Montgomery' in response

    def test_geocoder_council(self):
        response = self.app.get(url(controller='people', action='search', address=self.degraw))
        assert 'David Yassky' in response

    def test_no_address(self):
        response = self.app.get(url(controller='people', action='search'))
        assert 'No results found' in response

    def test_bogus_address(self):
        response = self.app.get(url(controller='people', action='search', address='Zbasp89ba~#$'))
        assert 'No results found' in response


    def test_address_out_of_known_world(self):
        response = self.app.get(url(controller='people', action='search', address='90210'))
        assert 'No results found' in response

    def test_address_ambiguous(self):
        response = self.app.get(url(controller='people', action='search', address='main st.'))
        assert 'Did you mean one of these addresses?' in response

