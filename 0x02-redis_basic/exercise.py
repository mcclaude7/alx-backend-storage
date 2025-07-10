#!/usr/bin/env python3
"""
Module for caching data using Redis.
Implements methods to store, retrieve, and count method calls.
"""

import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.
    Uses Redis INCR with method's qualified name as key.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Cache class for storing and retrieving data from Redis."""

    def __init__(self):
        """Initialize Redis client and flush database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key.

        Args:
            data: The data to store (str, bytes, int, or float).

        Returns:
            The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        Retrieve data from Redis and optionally apply a conversion function.

        Args:
            key: Redis key.
            fn: Optional function to transform the data.

        Returns:
            The retrieved data or None if key doesn't exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """
        Retrieve data as UTF-8 string from Redis.

        Args:
            key: Redis key.

        Returns:
            The decoded string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve data as integer from Redis.

        Args:
            key: Redis key.

        Returns:
            The integer value.
        """
        return self.get(key, fn=int)
