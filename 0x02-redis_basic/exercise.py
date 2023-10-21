#!/usr/bin/env python3
"""
This script offers a Redis cache management class with
storage, retrieval, method call counting, history recording,
and replay capabilities.
"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
    This decorator tracks and increments the call count each time
    the decorated function is invoked.

    Args:
        method (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function, which now includes
        call count tracking.
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        This wrapper function adds functionality to count the number
        of times the decorated function is called.

        Args:
            self: The object instance.
            *args: The arguments passed to the function.
            **kwargs: The keyword arguments passed to the function.

        Returns:
            The return value of the decorated function.
        """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    This decorator captures the input arguments and the return value
    of the decorated function and stores them in Redis for later
    analysis or replay.

    Args:
        method (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function with input
        and output recording capabilities.
    """
    key = "{}:inputs".format(method.__qualname__)
    outputs = "{}:outputs".format(method.__qualname__)

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        This wrapper function extends the decorated function's behavior
        by capturing the input arguments and the return value,
        and recording them for analysis.

        Args:
            self: The object instance.
            *args: The arguments passed to the decorated function.
            **kwargs: The keyword arguments passed to the decorated function.

        Returns:
            The return value of the decorated function.

        Notes:
            This wrapper is used in conjunction with the `call_history` decorator
            to log function calls and their corresponding input and output values
            in Redis.
        """
        input_data = str(args)
        data = method(self, *args, **kwargs)
        output_data = str(data)

        self._redis.rpush(key, input_data)
        self._redis.rpush(outputs, output_data)

        return data


def replay(method: Callable) -> None:
    """
    Replays the historical function calls stored in Redis
    and prints the results.

    This decorator function replays the recorded function calls
    and their input arguments, along with the corresponding
    output values, stored in Redis.

    Args:
        method (Callable): The function to be decorated.

    Returns:
        None
    """
    name = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(name).decode("utf-8")

    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)

    print("{} was called {} times:".format(name, calls))

    for i, o in zip(inputs, outputs):
        try:
            input_str = i.decode('utf-8')
        except AttributeError:
            input_str = i

        try:
            output_str = o.decode('utf-8')
        except AttributeError:
            output_str = o

        print("{}(*{}) -> {}".format(name, input_str, output_str))


class Cache:
    """
    A class for managing Redis cache operations.

    This class provides methods for interacting with a Redis cache.

    Methods:
        - __init__(self): Initialize the Redis client
        and flush the database.
    """
    def __init__(self) -> None:
        """
        Initialize a Redis client and flush the database.

        This method creates an instance of the Redis client and clears
        the database, ensuring a clean slate for cache operations.

        Attributes:
            self._redis (redis.Redis): Redis client instance.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in the Redis cache.

        Args:
            data (Union[str, bytes, int, float]): The data to store
            in the cache.

        Returns:
            str: The key used for storing the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float, None]:
        """
        Retrieves data from the Redis cache.

        Args:
            key (str): The key associated with the data.
            fn (Optional[Callable]): An optional callable function
            to transform the data.

        Returns:
            Union[str, bytes, int, float, None]: The stored data,
            optionally transformed by fn.
        """
        data = self._redis.get(key)

        if data is not None and fn is not None and callable(fn):
            return fn(data)

        return data

    def get_str(self, key: str) -> str:
        """
        Retrieves data as a string from the Redis cache.

        Args:
            key (str): The key associated with the data.

        Returns:
            str: The stored data as a string,
            decoded from bytes if necessary.
        """
        data = self.get(key)

        try:
            data = data.decode('utf-8')
        except AttributeError:
            pass

        return data

    def get_int(self, key: str) -> int:
        """
        Retrieves data as an integer from Redis cache.

        Args:
            key (str): The key associated with the data.

        Returns:
            int: The stored data, converted to an integer.
        """
        data = self.get(key, int)
        return data
