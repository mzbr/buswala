def make_list_from_xml(root):
    agency_list = []
    for child in root.getchildren():
        agency_list.append(child.attrib)
    return agency_list