from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource
from feed import *
import os
import retriever as r
import xml.etree.ElementTree as ET

app = Flask(__name__)
api = Api(app)

class Agency(Resource):
    
    def get(self):
        root = ET.fromstring(r.get_agencies())
        json = make_list_from_xml(root)
        return json

class Route(Resource):
    
    def get(self, agency_tag):
        root = ET.fromstring(r.get_routes(agency_tag))
        json = make_list_from_xml(root)
        return json
        
class Direction(Resource):
    
    def get(self, agency_tag, route_tag):
        root = ET.fromstring(r.get_directions(agency_tag, route_tag))
        json = make_list_from_xml(root)
        return json

api.add_resource(Agency, '/','/agencies', '/agencies/')
api.add_resource(Route,'/routes/<agency_tag>','/routes/<agency_tag>/')
api.add_resource(Direction, '/directions/<agency_tag>/<route_tag>','/directions/<agency_tag>/<route_tag>/')

if __name__ == '__main__':
    app.run(debug=True,host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',80)))