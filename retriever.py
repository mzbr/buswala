from constants import *
import requests

def get_agencies():
    response = requests.get(AGENCY_LIST_URL)
    return response.text
    
def get_routes(agency_tag):
    return

def get_directions(agency_tag,route_tag):
    return

