# -*- coding: utf-8 -*-
from pymongo import MongoClient
from pymongo import ReadPreference

client = MongoClient(
    "mongodb://10.0.10.2:27017,10.0.10.3:27017,10.0.10.4/?replicaSet=rs0",
    read_preference=ReadPreference.SECONDARY_PREFERRED,
)

print client.read_preference

print list(client.operation_log["activity"].find({}, projection={"_id": False, "object_id": False}, sort=[("modify_at", -1), ]))
