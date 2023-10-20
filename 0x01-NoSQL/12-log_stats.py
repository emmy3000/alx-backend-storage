#!/usr/bin/env python3

"""
Script provides statistics about Nginx logs stored in MongoDB

Database: logs, Collection: nginx, Display results as shown in the example
- First line: x logs, x number of documents in this collection
- Second line: Methods
- Five lines with method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
- One line with method=GET, path=/status
"""
from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """
    Provide statistics about Nginx logs stored in MongoDB.

    :param mongo_collection: The pymongo collection object.
    :param option: (Optional) Filter logs by method.
    """
    if option:
        value = mongo_collection.count_documents({"method": option})
        print("\tmethod {}: {}".format(option, value))
    else:
        total_logs = mongo_collection.count_documents({})
        print("{} logs".format(total_logs))
        print("Methods:")
        for method in METHODS:
            log_stats(mongo_collection, method)
        status_check = mongo_collection.count_documents(
            {"method": "GET", "path": "/status"})
        print("method=GET, path=/status: {}".format(status_check))


if __name__ == "__main":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)
