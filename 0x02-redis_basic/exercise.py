#!/usr/bin/env python3
"""Module for caching data with Redis"""
import redis
import uuid
from typing import Union, Callable, Optional, Any


class Cache:
    """Cache class that stores data in Redis"""

    def __init__(self):
        """Initialize Redis connection and flush database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis using a random key

        Args:
            data: The data to store (str, bytes, int, or float)

        Returns:
            The key as a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        Retrieve data from Redis and optionally apply a conversion function.

        Args:
            key (str): The Redis key.
            fn (Callable, optional): Function to convert the data back to the desired format.

        Returns:
            Any: The original data, or None if key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """
        Retrieve string data from Redis.

        Args:
            key (str): The Redis key.

        Returns:
            str: The decoded string value.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve integer data from Redis.

        Args:
            key (str): The Redis key.

        Returns:
            int: The integer value.
        """
        return self.get(key, fn=int)
