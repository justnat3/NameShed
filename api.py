import os
import random
import string
import sys

from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from NameGen import Drive, addPrefix

app = Flask(__name__) 
api = Api(app)

#endpoints
class Hello(Resource):
    def get(self):
        payload = {
            'response': 'Hello world'
        }
        return jsonify(payload)

class WriteName(Resource):
    def get(self):
        defaultSize = 10
        NameGen = Drive(defaultSize)
        payload = {
            "Name": f'{NameGen}'
        }
        return jsonify(payload)

#routes
api.add_resource(Hello, '/hello')
api.add_resource(WriteName, '/namegen')

#Driver code
if __name__ == "__main__":
    app.run(port='5001')
else:
    print('stop that')