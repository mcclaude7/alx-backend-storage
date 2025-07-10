#!/usr/bin/env python3
# """
# Main file
# """
# import redis

# Cache = __import__('exercise').Cache

# cache = Cache()

# data = b"hello"
# key = cache.store(data)
# print(key)

# local_redis = redis.Redis()
# print(local_redis.get(key))

#!/usr/bin/env python3
# from exercise import Cache

# cache = Cache()

# TEST_CASES = {
#     b"foo": None,
#     123: int,
#     "bar": lambda d: d.decode("utf-8")
# }

# for value, fn in TEST_CASES.items():
#     key = cache.store(value)
#     result = cache.get(key, fn=fn)
#     print(f"Stored: {value!r} ➜ Retrieved: {result!r}")
#     assert result == value

#!/usr/bin/env python3
""" Main file """

from exercise import Cache

cache = Cache()

# First call
cache.store(b"first")
print(cache.get(cache.store.__qualname__))

# More calls
cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))
