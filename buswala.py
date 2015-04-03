from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource
from feed import *
import os

app = Flask(__name__)
api = Api(app)

class Agency(Resource):
    
    def get(self):
        return get_agencies()
        

api.add_resource(Agency, '/','/agencies', '/agencies/')

if __name__ == '__main__':
    app.run(debug=True,host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',80)))