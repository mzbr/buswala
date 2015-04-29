from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource
from jsonify import *
import os
import retriever as r
import xml.etree.ElementTree as ET

app = Flask(__name__)
api = Api(app)


class Agency(Resource):
    
    def get(self):
        root = ET.fromstring(r.get_agencies())
        json_resp = get_error(root) or convert_to_json(root)
        return json_resp


class Route(Resource):
    
    def get(self, agency_tag):
        root = ET.fromstring(r.get_routes(agency_tag))
        json_resp = get_error(root) or convert_to_json(root)
        return json_resp

        
class Direction(Resource):
    
    def get(self, agency_tag, route_tag):
        root = ET.fromstring(r.get_directions(agency_tag, route_tag))
        json_resp = get_error(root) or get_directions_in_json(root)
        return json_resp


class Stop(Resource):
    
    def get(self, agency_tag, route_tag, direction_tag):
        root = ET.fromstring(r.get_stops(agency_tag,route_tag))
        json_resp = get_error(root) or r.get_stops_in_json(root,direction_tag)
        return json_resp    


api.add_resource(Agency,'/agencies/')
api.add_resource(Route,'/routes/<agency_tag>/')
api.add_resource(Direction, '/directions/<agency_tag>/<route_tag>/')
api.add_resource(Stop, '/stops/<agency_tag>/<route_tag>/<direction_tag>/')

if __name__ == '__main__':
    app.run(debug=True,host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',80)))

