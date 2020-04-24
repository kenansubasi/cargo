import json

from .app import mongo
from .constants import FLASK_ENV, FIXTURE_DIR


def load_data():
    if FLASK_ENV != "development":
        print("You must enable DEBUG mode to run this command.")
        return

    fixtures = [  # order is important!
        "cities"
    ]
    for fixture in fixtures:
        path = f"{FIXTURE_DIR}/{fixture}.json"
        print(f"Inserting fixture '{fixture}'...")
        print(path)

        with open(path) as f:
            file_data = json.load(f)

        mongo.db[fixture].remove()
        mongo.db[fixture].insert_many(file_data)
