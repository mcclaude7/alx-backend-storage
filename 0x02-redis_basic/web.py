#!/usr/bin/env python3
"""
Module that provides a caching layer using Redis and tracks
access frequency to URLs.
"""

import redis
import requests
from functools import wraps
from typing import Callable
from urllib.parse import quote

# Connect to Redis
redis_client = redis.Redis(host='127.0.0.1', port=6379, decode_responses=False)


def count_access(method: Callable) -> Callable:
    """
    Decorator to count how many times a URL has been accessed.
    It stores the count in Redis with the key format: "count:{url}".
    """

    @wraps(method)
    def wrapper(url: str) -> str:
        encoded_url = quote(url, safe="")
        count_key = f"count:{encoded_url}"
        redis_client.incr(count_key)
        print(f"[COUNT] Incremented key: {count_key}")
        return method(url)

    return wrapper


@count_access
def get_page(url: str) -> str:
    """
    Retrieves the HTML content of a given URL and caches it in Redis
    for 10 seconds. If cached, returns the cached content.

    Args:
        url (str): The web URL to fetch content from.

    Returns:
        str: HTML content of the page.
    """
    encoded_url = quote(url, safe="")
    cache_key = f"cached:{encoded_url}"

    cached = redis_client.get(cache_key)
    if cached:
        print(f"[CACHE HIT] Key: {cache_key}")
        return cached.decode('utf-8')

    print(f"[CACHE MISS] Fetching from web: {url}")
    response = requests.get(url)
    content = response.text

    redis_client.setex(cache_key, 10, content)
    print(f"[CACHE SET] Key: {cache_key}, TTL: 10 seconds")
    return content


def cache_result(method: Callable) -> Callable:
    """
    Decorator to cache the HTML result of a URL for 10 seconds.
    If the URL is already cached, returns the cached content.
    """

    @wraps(method)
    def wrapper(url: str) -> str:
        encoded_url = quote(url, safe="")
        cache_key = f"cached:{encoded_url}"

        cached_html = redis_client.get(cache_key)
        if cached_html:
            print(f"[CACHE RESULT DECORATOR HIT] "
                  f"Key: {cache_key}")
            return cached_html.decode("utf-8")

        result = method(url)
        redis_client.setex(cache_key, 10, result)
        print(f"[CACHE RESULT DECORATOR SET] "
              f"Key: {cache_key}, TTL: 10 seconds")
        return result

    return wrapper


if __name__ == "__main__":
    test_url = (
        "http://slowwly.robertomurray.co.uk/delay/3000/url/"
        "http://example.com"
    )
    print("Fetching page...")
    content = get_page(test_url)
    print("Content received (first 200 characters):")
    print(content[:200])
