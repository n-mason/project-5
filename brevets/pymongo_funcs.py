"""
Pymongo Functions to insert and fetch brevet data from MongoDB database.
This code is based off of the helpful example code written
by Ali Hassani, found at: https://github.com/UO-CIS322/TodoListApp

CS 322 - Universty of Oregon

Author: Nathaniel Mason
"""

import os
from pymongo import MongoClient

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.mybrevetsdb

collection = db.brevets

def brevet_insert(start_time_str, brev_dist, checkpoints):
    """
    Inserts brevet data into the database under the collection "brevets".

    Inputs a start date (string), brevet distance (int) and checkpoints (list of dictionaries)

    Returns unique ID assigned to document by mongo
    """
    record = {"start_time": start_time_str, "brevet_distance": brev_dist, "checkpoints": checkpoints}
    output = collection.insert_one(record)
    _id = output.inserted_id # now _id will contain the primary key that was assigned by mongo upon insertino of receord into database
    return str(_id)


def brevet_fetch():
    """
    Fetches the newest document in "brevets" collection in database "mybrevetsdb".

    Returns start date (string) and items (list of dictionaries) as a tuple

    """
    brevet_data_set = collection.find().sort("_id", -1).limit(1) # Sort by primary key in desccending order and limit to 1 
    # document (which is a row in our case). Taking these steps means that we will find the newest inserted document

    # brevet_data_set is a PyMongo cursor, so we iterate through it to make sure we get all entries (possible to have only one entry)
    for brev_data in brevet_data_set:
        # Each piece of brev data is stored as a start time, brevet distance and checkpoints dictionary
        return brev_data["start_time"], brev_data["brevet_distance"], brev_data["checkpoints"]