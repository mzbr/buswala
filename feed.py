import retriever as r
import xml.etree.ElementTree as ET

def get_agencies():
    root = ET.fromstring(r.get_agencies())
    return make_agency_list(root)
    
def make_agency_list(root):
    agency_list = []
    for child in root.getchildren():
        agency_list.append(child.attrib)
    return agency_list