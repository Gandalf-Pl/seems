# coding: utf8

from pymongo import MongoClient, Connection


# mongodb uri: "mongodb://user:pass@example.com/my_database/"
uri = "mongodb://localhost:27017/test_order"

client = MongoClient(uri)

# get default database defined in the uri
db = client.get_default_database()

print db


conn = Connection(uri)

db = conn.get_default_database()

print "conn db", db
