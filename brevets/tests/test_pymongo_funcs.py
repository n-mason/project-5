"""
Nose tests for pymongo_functions.py
"""

from pymongo_funcs import brevet_insert, brevet_fetch
import arrow
import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_pymongo_test1():
    #def brevet_insert(start_time, brevet_dist, controls) where 
    #controls is a list of controls (checkpoints) to insert
    start_time = arrow.get("2023-02-18 08:00", "YYYY-MM-DD HH:mm")
    dist = 200
    checkpoints = {
                    0: (start_time, start_time.shift(hours=1)),
                    50: (start_time.shift(hours=1, minutes=28), start_time.shift(hours=3, minutes=30)),
                    150: (start_time.shift(hours=4, minutes=25), start_time.shift(hours=10)),
                    200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13, minutes=30)),
                    }

    checkpoints_str = {}

    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        
        checkpoint_open_str = checkpoint_open.format("YYYY-MM-DDTHH:mm")
        checkpoint_close_str = checkpoint_close.format("YYYY-MM-DDTHH:mm")

        km_str = str(km)
        checkpoints_str[km_str] = [checkpoint_open_str, checkpoint_close_str]

    start_time_str = start_time.format("YYYY-MM-DDTHH:mm")
    
    data_to_insert = {"start_time": start_time_str, "brevet_distance": dist, "checkpoints": checkpoints_str}
    brevet_insert(start_time_str, dist, checkpoints_str)

    fetch_result = brevet_fetch(start_time_str, dist, checkpoints_str)
    # fetch_result also contains the "id" key that gets automatically added to the database, so need to filter that out
    fetch_result_filtered = {}
    
    for key, value in fetch_result.items():
        if key == "_id": # filter out the _id key
            pass
        else:
            fetch_result_filtered[key] = value

    #print(data_to_insert)
    #print("----------------------------------------")
    #print(fetch_result_filtered)

    assert(data_to_insert == fetch_result_filtered)


def test_pymongo_test2():
    start_time = arrow.get("2023-04-04 13:00", "YYYY-MM-DD HH:mm")
    dist = 300
    checkpoints = {
                    0: (start_time, start_time.shift(hours=1)),
                    60: (start_time.shift(hours=1, minutes=46), start_time.shift(hours=4)),
                    120: (start_time.shift(hours=3, minutes=32), start_time.shift(hours=8)),
                    180: (start_time.shift(hours=5, minutes=18), start_time.shift(hours=12)),
                    240: (start_time.shift(hours=7, minutes=8), start_time.shift(hours=16)),
                    300: (start_time.shift(hours=9), start_time.shift(hours=20)),
                    }

    checkpoints_str = {}

    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        
        checkpoint_open_str = checkpoint_open.format("YYYY-MM-DDTHH:mm")
        checkpoint_close_str = checkpoint_close.format("YYYY-MM-DDTHH:mm")

        km_str = str(km)
        checkpoints_str[km_str] = [checkpoint_open_str, checkpoint_close_str]

    start_time_str = start_time.format("YYYY-MM-DDTHH:mm")
    
    data_to_insert = {"start_time": start_time_str, "brevet_distance": dist, "checkpoints": checkpoints_str}
    brevet_insert(start_time_str, dist, checkpoints_str)

    fetch_result = brevet_fetch(start_time_str, dist, checkpoints_str)
    fetch_result_filtered = {}
    
    for key, value in fetch_result.items():
        if key == "_id": # filter out the _id key
            pass
        else:
            fetch_result_filtered[key] = value
