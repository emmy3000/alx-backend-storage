#!/usr/bin/env python3
"""
Script returns all students sorted by their average scores.
"""


def top_students(mongo_collection):
    """
    Return all students sorted by their average scores.
    :param mongo_collection: The MongoDB collection containing
    student data.
    :return: A list of students sorted by their average scores
    in descending order.
    """
    return mongo_collection.aggregate([
        {
            "$project":
            {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort":
            {
                "averageScore": -1
            }
        }
    ])
