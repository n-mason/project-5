import os
from pymongo import MongoClient

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.mybrevetsdb

def brevet_insert(start_time_arrow, brev_dist, chckpts):
    client.db.brevets.insert({start_time: start_time_arrow, brevet_distance: brev_dist, checkpoints: chckpts})

def brevet_fetch(start_time_arrow, brev_dist, chckpts):
    client.db.brevets.find({start_time: start_time_arrow, brevet_distance: brev_dist, checkpoints: chckpts})