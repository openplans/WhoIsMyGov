from purplevoter.tests import url, TestController

class TestPeopleController(TestController):

    degraw = '669 degraw st., 11217'

    mockgeocoder_results = []
    extra_environ = {'mockgeocoder.results': mockgeocoder_results}

#     def test_geocoder_senate(self):
#         response = self.app.get(url(controller='people', action='search', address=self.degraw, level_name='federal'))
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
        self.mockgeocoder_results[:] = [(u'669 Degraw St, Brooklyn, NY 11217, USA',
                                         (40.678329400000003, -73.981242499999993))]
        response = self.app.get(url(controller='people', action='search', address=self.degraw))
        assert 'David Yassky' in response

    def test_geocoder_races(self):
        self.mockgeocoder_results[:] = [(u'669 Degraw St, Brooklyn, NY 11217, USA',
                                         (40.678329400000003, -73.981242499999993))]
        response = self.app.get(url(controller='people', action='search', address=self.degraw))
        assert isinstance(response.c.races, list)
        assert response.c.races, "got empty races list"
        self.assertEqual(len(response.c.races), 4)
        offices = sorted(r.office for r in response.c.races)
        assert offices[0] == u'City Council'
        assert offices[1] == u'Comptroller'
        assert offices[2] == u'Mayor'
        assert offices[3] == u'Public Advocate'


    def test_no_address(self):
        self.mockgeocoder_results[:] = []
        response = self.app.get(url(controller='people', action='search'))
        assert 'No results found' in response

    def test_bogus_address(self):
        response = self.app.get(url(controller='people', action='search', address='Zbasp89ba~#$'))
        assert 'No results found' in response

    def test_address_out_of_known_world(self):
        self.mockgeocoder_results[:] = [(u'Beverly Hills, CA 90210, USA',
                                      (34.103003200000003, -118.4104684))]
        response = self.app.get(url(controller='people', action='search', address='90210'))
        assert 'No results found' in response

    def test_address_ambiguous(self):
        self.mockgeocoder_results[:] = [
            (u'Main St, New York, NY 10044, USA', (40.761251999999999, -73.950389000000001)),
            (u'Main St, Madawaska, ME 04756, USA', (47.299903999999998, -68.377725999999996)),
            (u'Main St, Green Bay, WI, USA', (44.461621999999998, -87.953372000000002)),
            (u'Main St, NV, USA', (38.926498000000002, -119.728736)),
            (u'Main St, Lugoff, SC 29078, USA', (34.206927999999998, -80.728324000000001)),
            (u'Main St, Bamberg, SC 29003, USA', (33.254896000000002, -81.075939000000005)),
            (u'Main St, Columbia, SC, USA', (34.031680000000001, -81.042098999999993)),
            (u'Main St, Springville, AL 35146, USA', (33.766407000000001, -86.479605000000006)),
            (u'Main St, ME, USA', (44.884884, -68.671289000000002)),
            (u'Main St, ME, USA', (47.303555000000003, -68.150024999999999))]
        response = self.app.get(url(controller='people', action='search', address='main st.'))
        assert 'Did you mean one of these addresses?' in response




class TestPeopleControllerJsonOutput(TestController):

    lafayette = '148 lafayette st., new york, ny'

    mockgeocoder_results = []
    extra_environ = {'mockgeocoder.results': mockgeocoder_results}
 
    def _search_json(self, *args, **kw):
        response = self.app.get(url(controller='people', action='search_json', *args, **kw))
        return response
        
    def test_no_address(self):
        response = self._search_json()
        assert response.json == []

    def test_bogus_address(self):
        response = self._search_json(address='Zbasp89ba~#$')
        assert response.json == []

    def test_address_out_of_known_world(self):
        response = self._search_json(address='90210')
        assert response.json == []

    def test_address_ambiguous(self):
        self.mockgeocoder_results[:] = [
            (u'Main St, Springfield, CO 81073, USA',
             (37.404052999999998, -102.61655399999999)),
            (u'Main St, Springfield, OR, USA',
             (44.045764400000003, -122.96185699999999)),
            (u'Main St, Springfield, MA, USA',
             (42.106045000000002, -72.597044499999996)),
            (u'Main St, Springfield, IL 62711, USA',
             (39.709083999999997, -89.704749000000007)),
            (u'Main St, Springfield, LA 70462, USA',
             (30.438205, -90.568635999999998)),
            (u'Main St, Springfield, MA 01151, USA',
             (42.159067, -72.4967015)), 
            (u'Main St, Springfield, NJ 07081, USA',
             (40.712091000000001, -74.307867000000002)), 
            (u'Main St, Springfield, VT 05156, USA',
             (43.296849000000002, -72.481633000000002))]

        response = self._search_json(address='main st., springfield')
        assert response.json == []
