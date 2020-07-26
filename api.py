import random
import string

from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from NameGen import Drive, addPrefix

app = Flask(__name__) 
api = Api(app)

#endpoints
@app.errorhandler(404)
def page_not_found(e):
    return '<h1>This Endpoint does not Exist</h1>', 404

class Health(Resource):
    def get(self):
        return {'response': 'Thread Alive'}

class WriteName(Resource):
    def get(self):
        # Size = 10
        NameGen = Drive(5)
        payload = {
            "Name": f'{NameGen}'
        }
        return jsonify(payload)

#Routes
api.add_resource(Health, '/', '/health')
api.add_resource(WriteName, '/namegen')
    
#Driver code
if __name__ == "__main__":
    app.run(port='5001')
