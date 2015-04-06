import requests, json, unittest

TEST_URL = "http://buswala-mzbr.c9.io/"

class BaseURLTestCase(unittest.TestCase):

    def setUp(self):
        url = TEST_URL + "agencies"
        response = requests.get(url)
        self.json_resp = json.loads(response.text)
        self.agency_title = "Toronto Transit Commission"
        self.region_title = "Ontario"
        self.short_title = "Toronto TTC"
        self.agency_tag = 'ttc'
    
    def testReturnsDict(self):
        assert isinstance(self.json_resp, dict)
        
    def testDictIsNotEmpty(self):
        assert len(self.json_resp) > 0
        
    def testValidAgencyTitle(self):
        assert self.json_resp[self.agency_tag]['title'] == self.agency_title
    
    def testValidAgencyRegionTitle(self):
        assert self.json_resp[self.agency_tag]['regionTitle'] == self.region_title
        
    def testValidAgencyShortTitle(self):
        assert self.json_resp[self.agency_tag]['shortTitle'] == self.short_title
        
        
class AgencyURLTestCase(BaseURLTestCase):
    
    def setUp(self):
        url = TEST_URL + "agencies"
        response = requests.get(url)
        self.json_resp = json.loads(response.text)
        self.agency_title = "San Francisco Muni"
        self.region_title = "California-Northern"
        self.short_title = "SF Muni"
        self.agency_tag = "sf-muni"
        
        
class RouteTestCase(unittest.TestCase):

    def setUp(self):
        self.agency_tag = "ttc"
        self.route_title = "80-Queensway"
        self.route_tag = "80"
        url = TEST_URL + "routes/" + self.agency_tag
        response = requests.get(url)
        self.json_resp = json.loads(response.text)
    
    def testReturnsDict(self):
        assert isinstance(self.json_resp, dict)
        
    def testValidAgency(self):
        assert self.json_resp[self.route_tag]['title'] == self.route_title
    
if __name__ == "__main__":
    unittest.main()