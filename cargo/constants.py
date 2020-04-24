import os

# Base
FLASK_ENV = os.environ.get("FLASK_ENV", "development")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURE_DIR = os.path.join(BASE_DIR, "fixtures", "data")

# Database
MONGODB_HOSTNAME=os.environ["MONGODB_HOSTNAME"]
MONGODB_PORT=os.environ["MONGODB_PORT"]
MONGODB_DATABASE=os.environ["MONGO_INITDB_DATABASE"]
MONGO_URI = "mongodb://{hostname}:{port}/{database}".format(
    hostname=MONGODB_HOSTNAME,
    port=MONGODB_PORT,
    database=MONGODB_DATABASE
)
