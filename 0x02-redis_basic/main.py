#!/usr/bin/env python3
"""
Test script for web.py module.
"""

from web import get_page
import time

# Test URL simulating a slow response
test_url = (
    "http://slowwly.robertomurray.co.uk/delay/3000/url/http://example.com"
)

print("First request (should take ~3 seconds)...")
html1 = get_page(test_url)
print(f"Length of content: {len(html1)}")

print("\nSecond request (should be instant, cached)...")
html2 = get_page(test_url)
print(f"Length of content: {len(html2)}")

# Sleep to allow Redis cache to expire
print("\nSleeping for 11 seconds to expire cache...")
time.sleep(11)

print("\nThird request (should take ~3 seconds again)...")
html3 = get_page(test_url)
print(f"Length of content: {len(html3)}")
