from constants import *

def convert_to_json(root):
    json_dict = {}
    for child in root.getchildren():
        json_dict[child.get('tag')] = make_dict_of_attribs_except_tag(child)
    return json_dict
    
def get_directions_in_json(root):
    directions = root.findall("./route/direction")
    return list_to_json_dict(directions)
    
def make_dict_of_attribs_except_tag(elem):
    temp_dict = make_dict_of_attribs(elem)
    del temp_dict['tag']
    return temp_dict

def make_dict_of_attribs(elem):
    attrib_dict = {}
    for key,val in elem.items():
        attrib_dict[key] = val
    return  attrib_dict
    
def make_list_from_xml(root):
    agency_list = []
    for child in root.getchildren():
        agency_list.append(child.attrib)
    return agency_list

def list_to_json_dict(elem_list):
    directions = {}
    for elem in elem_list:
        directions[elem.get('tag')] = make_dict_of_attribs_except_tag(elem)
    return directions
    
def make_route_config_url(agency_tag, route_tag):
    return ROUTE_CONFIG_URL + agency_tag + "&r=" + route_tag
    
def get_error(root):
    errors = root.find("Error")
    if not errors == None:
        return remove_newlines(errors.text)
    else:
        return None
        
def remove_newlines(text):
    return text.strip().replace('\n', '')