#!/usr/bin/env python3
"""
Script lists all the documents in a collection
"""


def list_all(mongo_collection):
    """
    List all documents in a collection.

    :param mongo_collection: The pymongo collection object.
    :return: A list of documents in the collection.
    """
    documents = mongo_collection.find()
    return documents
