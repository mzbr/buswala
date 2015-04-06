from constants import *

def convert_to_json(root):
    agencies = {}
    for child in root.getchildren():
        agencies[child.get('tag')] = make_dictionary(child)
    return agencies
    
def make_dictionary(elem):
    attrib_dict = {}
    for key,val in elem.items():
        if not key == 'tag':
            attrib_dict[key] = val
            
    return  attrib_dict
    
def make_list_from_xml(root):
    agency_list = []
    for child in root.getchildren():
        agency_list.append(child.attrib)
    return agency_list
    
    
def make_route_config_url(agency_tag, route_tag):
    return ROUTE_CONFIG_URL + agency_tag + "&r=" + route_tag