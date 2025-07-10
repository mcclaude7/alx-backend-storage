#!/usr/bin/env python3
"""
Test script for the get_page function in web.py.
Demonstrates caching and access counting.
"""

from web import get_page
import time
import redis

test_url = (
    "http://slowwly.robertomurray.co.uk/delay/3000/"
    "url/http://example.com"
)

print("First request (should take ~3 seconds)...")
html1 = get_page(test_url)
print(f"Length of content: {len(html1)}")

print("\nSecond request (should be instant, cached)...")
html2 = get_page(test_url)
print(f"Length of content: {len(html2)}")

print("\nSleeping for 11 seconds to expire cache...")
time.sleep(11)

print("\nThird request (should take ~3 seconds again)...")
html3 = get_page(test_url)
print(f"Length of content: {len(html3)}")

# Optional: display access count
r = redis.Redis()
access_count = r.get(f"count:{test_url}")
if access_count:
    print(f"\nURL accessed {int(access_count)} times")
