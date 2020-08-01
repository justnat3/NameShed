import random
import string

from flask import Flask, got_request_exception, jsonify, request
from flask_restful import Api, Resource, reqparse

from generator import Drive, addPrefix

errors = {
    '500 Handler': {
        'message': 'Something went horribly wrong!',
        'status': 500
    }
}

app = Flask(__name__)
api = Api(app, errors=errors)

# endpoints
@app.errorhandler(404)
def page_not_found(e) -> int:
    return '<h1>This Endpoint does not Exist</h1>', 404


class Health(Resource):

    def get(self) -> object:
        return {'response': 'Thread Alive'}


class WriteName(Resource):

    def get(self) -> object:
        size = 10
        NameGen = Drive(size)
        payload = {
            "Name": f'{NameGen}'
        }
        return(jsonify(payload))


class PrefixGen(Resource):

    def get(self):
        prefix = request.args['prefix']
        size = request.args['size']
        if len(prefix) > 20:
            return None
        # return({"PrefixedName": f"{prefix.upper()}{Drive(int(size))}"})
        return({'PrefixResponse': f'{addPrefix(prefix, int(size))}'})


# Routes
api.add_resource(Health, '/', '/health')
api.add_resource(WriteName, '/namegen')
api.add_resource(PrefixGen, '/prefixGen')

# Driver code
if __name__ == "__main__":
    app.run(port='5001')
