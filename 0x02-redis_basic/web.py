#!/usr/bin/env python3
"""
Module for caching web pages using Redis with an expiration time
and tracking access count for each URL.
"""

import redis
import requests
from typing import Callable
from functools import wraps


# Create a Redis connection
r = redis.Redis()


def count_access(method: Callable) -> Callable:
    """
    Decorator to count how many times a URL is accessed.
    It increments the key 'count:{url}' in Redis.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        count_key = f"count:{url}"
        r.incr(count_key)
        return method(url)
    return wrapper


def cache_result(method: Callable) -> Callable:
    """
    Decorator to cache the HTML result of a URL for 10 seconds.
    If the URL is already cached, returns the cached content.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        cached_html = r.get(url)
        if cached_html:
            return cached_html.decode("utf-8")

        result = method(url)
        r.setex(url, 10, result)  # Cache with a TTL of 10 seconds
        return result
    return wrapper


@count_access
@cache_result
def get_page(url: str) -> str:
    """
    Fetch the HTML content of the specified URL.
    Uses Redis to cache the result and track access count.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: HTML content of the URL.
    """
    response = requests.get(url)
    return response.text
