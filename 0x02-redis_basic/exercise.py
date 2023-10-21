#!/usr/bin/env python3
"""
Basic redis implementation exercises.
"""
import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None):
        """
        Retrieve data from the Redis cache using the given key
        and optionally apply a conversion function.

        Args:
            key (str): The key to retrieve data from.
            fn (Callable, optional): A callable function to convert
            the retrieved data (default is None).

        Returns:
            Any: The data retrieved from the cache.
        """
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, key: str):
        """
        Retrieve a string from the Redis cache using the given key.

        Args:
            key (str): The key to retrieve the string from.

        Returns:
            str: The string retrieved from the cache.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str):
        """
        Retrieve an integer from the Redis cache using the given key.

        Args:
            key (str): The key to retrieve the integer from.

        Returns:
            int: The integer retrieved from the cache.
        """
        return self.get(key, fn=int)


# Test the new methods
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value

# Test get_str and get_int methods
key_str = cache.store("123")
key_int = cache.store(456)

assert cache.get_str(key_str) == "123"
assert cache.get_int(key_int) == 456
