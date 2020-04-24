from flask import Flask, make_response, jsonify
from flask_pymongo import PyMongo

from .constants import MONGODB_DATABASE, MONGO_URI


app = Flask(__name__)
app.config['MONGO_DBNAME'] = MONGODB_DATABASE
app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)


@app.route('/')
def index():
    return make_response(jsonify(message='Welcome to the Dockerized Flask MongoDB app!'), 200)


@app.route('/cities/')
def cityList():
    cities = mongo.db.cities.find()

    data = []
    for city in cities:
        item = {
            'id': str(city['_id']),
            'name': str(city['name'])
        }
        data.append(item)

    return make_response(jsonify(data), 200)
