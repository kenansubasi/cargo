import copy
import json
import math

from .app import mongo
from .constants import FLASK_ENV, FIXTURE_DIR


def load_data():
    if FLASK_ENV != "development":
        print("You must enable DEBUG mode to run this command.")
        return

    fixtures = [  # order is important!
        "cargo"
    ]
    for fixture in fixtures:
        path = f"{FIXTURE_DIR}/{fixture}.json"
        print(f"Inserting fixture '{fixture}'...")
        print(path)

        with open(path) as f:
            file_data = json.load(f)

        mongo.db[fixture].remove()
        mongo.db[fixture].insert_many(file_data)


class CargoHelper(object):

    def __init__(self, cargo_info, ordered=False):
        self.cargo_info = cargo_info if ordered else sorted(cargo_info, key=lambda item: item["price"])
        self.cities = set()
        self.shipment_companies = set()
        for item in self.cargo_info:
            self.cities.add(item["city"])
            self.shipment_companies.add(item["shipment_company"])
        self.city_count = len(self.cities)
        self.shipment_company_count = len(self.shipment_companies)
        self.cargo_count = math.ceil(self.city_count / self.shipment_company_count)

    def get_result(self):
        result = {}
        used_shipment_companies = []

        for item in self.cargo_info:
            if len(result) == self.city_count:
                break
            if (
                item["city"] not in result and
                used_shipment_companies.count(item["shipment_company"]) < self.cargo_count
            ):
                to_countries = copy.deepcopy(self.cities)
                to_countries.remove(item["city"])
                result.update({
                    item["city"]: {
                        "shipment_company": item["shipment_company"],
                        "price": item["price"],
                        "total_price": item["price"] * (self.city_count - 1),
                        "to_countries": sorted(to_countries)
                    }
                })
                used_shipment_companies.append(item["shipment_company"])

        return result
