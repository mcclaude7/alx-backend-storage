#!/usr/bin/env python3
"""
Main test file for web.py
"""

from web import get_page, r

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/3000/url/http://example.com"

    print("Fetching page 1st time (expect delay)...")
    html1 = get_page(url)
    print(f"Content length: {len(html1)}")

    print("\nFetching page 2nd time (should be cached)...")
    html2 = get_page(url)
    print(f"Content length: {len(html2)}")

    count_key = f"count:{url}"
    print(f"\nURL accessed {int(r.get(count_key))} times")
