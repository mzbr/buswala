from constants import *
from jsonify import *
import xml.etree.ElementTree as ET
import requests

def get_agencies():
    response = requests.get(AGENCY_LIST_URL)
    return response.text
    
def get_routes(agency_tag):
    response = requests.get(ROUTE_LIST_URL + agency_tag)
    return response.text

def get_directions(agency_tag,route_tag):
    url = make_route_config_url(agency_tag, route_tag)
    response = requests.get(url)
    return response.text