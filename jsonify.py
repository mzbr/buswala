from constants import *

def convert_to_json(root):
    json_dict = {}
    for child in root.getchildren():
        json_dict[child.get('tag')] = make_dict_of_attribs_except_tag(child)
    return json_dict
    
def get_directions_in_json(root):
    directions = root.findall("./route/direction")
    return list_to_json_dict(directions)
    
def get_stops_in_json(root,dir_tag):
    stops = root.findall("./route/direction[@tag='"+dir_tag+"']/stop")
    return list_to_json_dict(stops)
    




def list_to_json_dict(elem_list):
    directions = {}
    for elem in elem_list:
        directions[elem.get('tag')] = make_dict_of_attribs_except_tag(elem)
    return directions
    
def make_dict_of_attribs_except_tag(elem):
    temp_dict = make_dict_of_attribs(elem)
    del temp_dict['tag']
    return temp_dict

def make_dict_of_attribs(elem):
    attrib_dict = {}
    for key,val in elem.items():
        attrib_dict[key] = val
    return  attrib_dict

def make_dict_of_attribs(elem):
    attrib_dict = {}
    for key,val in elem.items():
        attrib_dict[key] = val
    return  attrib_dict

def get_error(root):
    errors = root.find("Error")
    if not errors == None:
        return remove_newlines(errors.text)
    else:
        return None
        
def remove_newlines(text):
    return text.strip().replace('\n', '')