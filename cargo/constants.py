import os

# Database
MONGODB_HOSTNAME=os.environ["MONGODB_HOSTNAME"]
MONGODB_PORT=os.environ["MONGODB_PORT"]
MONGODB_DATABASE=os.environ["MONGO_INITDB_DATABASE"]
MONGO_URI = "mongodb://{hostname}:{port}/{database}".format(
    hostname=MONGODB_HOSTNAME,
    port=MONGODB_PORT,
    database=MONGODB_DATABASE
)
