#!/usr/bin/env python3
"""Module for caching data with Redis"""
import redis
import uuid
from typing import Union


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
