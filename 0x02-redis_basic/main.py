# #!/usr/bin/env python3
# """
# Main test file for web.py
# """

# from web import get_page, r

# if __name__ == "__main__":
#     url = "http://slowwly.robertomurray.co.uk/delay/3000/url/http://example.com"

#     print("Fetching page 1st time (expect delay)...")
#     html1 = get_page(url)
#     print(f"Content length: {len(html1)}")

#     print("\nFetching page 2nd time (should be cached)...")
#     html2 = get_page(url)
#     print(f"Content length: {len(html2)}")

#     count_key = f"count:{url}"
#     print(f"\nURL accessed {int(r.get(count_key))} times")

#!/usr/bin/env python3
"""
Test script for web.py module.
"""

from web import get_page
import time

test_url = "http://slowwly.robertomurray.co.uk/delay/3000/url/http://example.com"

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
