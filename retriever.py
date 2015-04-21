from constants import *
from jsonify import *
import xml.etree.ElementTree as ET
import requests

def get_agencies():
    return get_response_text(AGENCY_LIST_URL)
    
def get_routes(agency_tag):
    return get_response_text(ROUTE_LIST_URL + agency_tag)

def get_directions(agency_tag,route_tag):
    url = make_route_config_url(agency_tag, route_tag)
    return get_response_text(url)
    
def get_response_text(url):
    response = requests.get(url)
    text = response.text
    print(text)
    return text