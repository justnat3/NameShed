import random
import string
import sys

from flask import Flask, got_request_exception, jsonify, request
from flask_restful import Api, Resource, reqparse

from namegen import Drive, addPrefix

app = Flask(__name__)
api = Api(app)

# endpoints
@app.errorhandler(404)
def page_not_found(e) -> int:
    return '<h1>This Endpoint does not Exist</h1>', 404


class Health(Resource):

    def get(self) -> object:
        return {'response': 'Thread Alive'}


class WriteName(Resource):

    def get(self) -> object:
        try:
            size = request.args['size']
            NameGen = Drive(int(size))
            payload = {
                "Name": f'{NameGen}'
            }
            return(jsonify(payload))
        except:
            return({'Error':'You may be missing ?size='})

class PrefixGen(Resource):

    def get(self):
        try:
            prefix = request.args['prefix']
            size = request.args['size']
            if len(prefix) > 20:
                return None
            return({'PrefixResponse': f'{addPrefix(prefix, int(size))}'})
        except:
            return {"Error": "Could not proccess request. Make sure you are using ?prefix=str&size=int"}


# Routes
api.add_resource(Health, '/', '/health')
api.add_resource(WriteName, '/namegen')
api.add_resource(PrefixGen, '/prefixGen')

