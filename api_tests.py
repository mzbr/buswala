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
        print("REQUEST URL:" + url)
        response = requests.get(url)
        self.json_resp = json.loads(response.text)
    
    def testReturnsDict(self):
        assert isinstance(self.json_resp, dict)
        
    def testValidAgency(self):
        assert self.json_resp[self.route_tag]['title'] == self.route_title


class DirectionTestCase(unittest.TestCase):
    
    def setUp(self):
        self.agency_tag = "sf-muni"
        self.route_tag = "N"
        self.dir_tag = "N____I_F00"
        self.dir_title = "Inbound to Caltrain via Downtown"
        self.dir_name = "Inbound"
        url = TEST_URL + "directions/" + self.agency_tag + "/" + self.route_tag
        response = requests.get(url)
        self.json_resp = json.loads(response.text)
    
    def testReturnsDict(self):
        assert isinstance(self.json_resp, dict)
        
    def testValidDirectionTitle(self):
        assert self.json_resp[self.dir_tag]['title'] == self.dir_title
        
    def testValidDirectionName(self):
        assert self.json_resp[self.dir_tag]['name'] == self.dir_name
        

class DirectionTestCaseTTC(DirectionTestCase):
    def setUp(self):
        self.agency_tag = "ttc"
        self.route_tag = "54"
        self.dir_tag = "54_0_54A"
        self.dir_title = "East - 54a Lawrence East towards Starspray"
        self.dir_name = "East"
        url = TEST_URL + "directions/" + self.agency_tag + "/" + self.route_tag
        response = requests.get(url)
        self.json_resp = json.loads(response.text)   
        
    
class DirectionTestInvalidDirection(unittest.TestCase):
    def setUp(self):
        self.agency_tag = "ttc"
        self.route_tag = "1234"
        url = TEST_URL + "directions/" + self.agency_tag + "/" + self.route_tag
        response = requests.get(url)
        self.json_resp = json.loads(response.text)
    
    def testReturnsError(self):
        assert self.json_resp == "Could not get route \"" + self.route_tag + "\" for agency tag \"" + self.agency_tag + "\". One of the tags could be bad."


class StopTestValidTTC(unittest.TestCase):
    def setUp(self):
        self.agency_tag = "ttc"
        self.route_tag = "54"
        self.dir_tag = "54_0_54A"
        self.stop_tag = "3758"
        self.stop_id = "5291"
        url = TEST_URL + "stops/" + self.agency_tag + "/" + self.route_tag + "/" + self.dir_tag
        response = requests.get(url)
        self.json_resp = json.loads(response.text)
        
    def testValidStopTitle(self):
        assert self.json_resp[self.stop_tag]['title'] == "Lawrence Ave East At Meadowvale Rd East Side"
    
    def testValidStopId(self):
        assert self.json_resp[self.stop_tag]['stopId'] == self.stop_id
        

if __name__ == "__main__":
    unittest.main()