from flask import Flask, request, make_response, jsonify
from flask_pymongo import PyMongo
from pymongo import ASCENDING

from .constants import MONGODB_DATABASE, MONGO_URI


app = Flask(__name__)
app.config['MONGO_DBNAME'] = MONGODB_DATABASE
app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)


@app.route('/')
def index():
    """
    It returns all endpoints.
    """
    data = {
        "Cargo Info": f"{request.url}info/",
        "Cargo Result": f"{request.url}result/"
    }

    return make_response(jsonify(data), 200)


@app.route("/info/")
def cargo_info():
    """
    It lists cargos' information.
    """
    cargo_info = mongo.db.cargo.find()

    data = []
    for item in cargo_info:
        data.append({
            "city": item["city"],
            "shipment_company": item["shipment_company"],
            "price": item["price"]
        })

    return make_response(jsonify(data), 200)


@app.route("/result/")
def cargo_result():
    """
    It returns optimum shipping list.
    """
    from .utils import CargoHelper
    cargo_info = mongo.db.cargo.find().sort("price", ASCENDING)

    cargo_helper = CargoHelper(list(cargo_info), ordered=True)
    result = cargo_helper.get_result()

    return make_response(jsonify(result), 200)
