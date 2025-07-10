#!/usr/bin/env python3
""" Main file """

#from exercise import Cache
Cache = __import__('exercise').Cache

cache = Cache()

# First call
cache.store(b"first")
print(cache.get(cache.store.__qualname__))

# More calls
cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))
