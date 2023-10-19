#!/usr/bin/env python3

"""
Script provides statistics about Nginx logs stored in MongoDB

Database: logs, Collection: nginx
- First line: x logs, x number of documents in this collection
- Second line: Methods
- Five lines with method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
- One line with method=GET, path=/status
- IPs: Top 10 most present IPs in the collection
"""
from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection):
    """
    Provide statistics about Nginx logs stored in MongoDB.

    :param mongo_collection: The pymongo collection object.
    """
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    for method in METHODS:
        method_count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    status_check = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"method=GET, path=/status: {status_check}")

    print("IPs:")
    top_ips = mongo_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)
