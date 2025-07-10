# 0x02. Redis basic

## Description

This project focuses on using **Redis** as a data storage solution and simple cache in Python. You’ll implement methods for storing, retrieving, and counting data operations while ensuring proper type handling and performance tracking using decorators.

---

## Learning Objectives

- How to use Redis for basic data storage and caching.
- How to interact with Redis from Python using the `redis-py` library.
- How to store different data types in Redis.
- How to use decorators to count method calls.
- How to use decorators to record method history.

---

## Requirements

- Ubuntu 18.04 LTS
- Python 3.7
- Redis server installed (`sudo apt-get install redis-server`)
- Redis Python client (`pip3 install redis`)
- PEP8 compliant (pycodestyle v2.5)
- All modules, classes, and methods are documented.
- All functions and coroutines are type-annotated.

---

## Files

| Filename        | Description |
|----------------|-------------|
| `exercise.py`  | Main module implementing Redis-based cache using a `Cache` class. |
| `main.py`      | Test file for running and verifying the cache functionality. |

---

## Tasks

### 0. Writing strings to Redis
- `Cache.store()` stores data (str, bytes, int, float) in Redis using a random key.
- Returns the key used for storage.

### 1. Reading from Redis and recovering original type
- `Cache.get()` retrieves data and optionally applies a conversion function.
- `Cache.get_str()` and `Cache.get_int()` retrieve string and integer values respectively.

### 2. Incrementing values
- Implements a `@count_calls` decorator to track how many times a method is called.
- Uses Redis `INCR` command and method `__qualname__` as the key.
- Decorates the `store()` method.

