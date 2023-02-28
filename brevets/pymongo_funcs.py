import os
from pymongo import MongoClient

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.mybrevetsdb

def brevet_insert(start_time_str, brev_dist, chckpts):
    record = {"start_time": start_time_str, "brevet_distance": brev_dist, "checkpoints": chckpts}
    db.brevets.insert_one(record)

def brevet_fetch(start_time_str, brev_dist, chckpts):
    request = {"start_time": start_time_str, "brevet_distance": brev_dist, "checkpoints": chckpts}
    mydict = db.brevets.find_one(request)
    return mydict