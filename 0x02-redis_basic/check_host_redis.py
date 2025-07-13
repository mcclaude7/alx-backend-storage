#!/usr/bin/env python3
import redis

r = redis.Redis(host='127.0.0.1', port=6379)
r.set('check_key', 'hello')
print("Key written to 127.0.0.1:6379")
