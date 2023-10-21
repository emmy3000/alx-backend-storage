#!/usr/bin/env python3
"""
Basic redis implementation exercises.
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    A class for interacting with a Redis cache.

    Attributes:
        _redis (redis.Redis): The Redis client instance.
    """

    def __init__(self):
        """
        Initialize the Cache instance and flush the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in the Redis cache and return the corresponding key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored
            in the cache.

        Returns:
            str: The key under which the data is stored in the cache.
        """
        key = str(uuid.uuid4())  # Generate a random key
        self._redis.set(key, data)  # Store data in Redis with the random key
        return key
