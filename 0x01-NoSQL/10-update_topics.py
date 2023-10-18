#!/usr/bin/env python3

"""
Script updates topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    Update topics of a school document based on the name.

    :param mongo_collection: The pymongo collection object.
    :param name: The name of the school to update.
    :param topics: A list of topics to set for the school.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
