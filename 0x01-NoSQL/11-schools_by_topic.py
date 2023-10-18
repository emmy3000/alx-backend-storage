#!/usr/bin/env python3

"""
Script returns a list of schools with a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Return a list of schools that have a specific topic.

    :param mongo_collection: The pymongo collection object.
    :param topic: The topic to search for.
    :return: A list of schools with the specified topic.
    """
    return mongo_collection.find({"topics": topic})
