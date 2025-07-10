# 0x02. Redis basic

## Description

This project introduces the use of **Redis** in Python for data storage and caching. It demonstrates how to use the `redis` Python package to interact with a Redis server, store different data types, and implement a simple cache layer using type-annotated methods.

---

## Learning Objectives

By completing this project, you will learn to:

- Use Redis for basic operations with Python
- Store and retrieve string, byte, int, and float values in Redis
- Create Redis keys dynamically
- Use Redis as a simple cache
- Apply type annotations in Python
- Write fully documented Python classes and functions

---

## Requirements

- Ubuntu 18.04 LTS
- Python 3.7
- `pycodestyle` version 2.5
- Redis server
- `redis` Python package

---

## Installation

To set up Redis and required dependencies on Ubuntu 18.04:

```bash
sudo apt-get update
sudo apt-get -y install redis-server
sudo sed -i "s/^bind .*/bind 127.0.0.1/" /etc/redis/redis.conf
sudo service redis-server start
pip3 install redis
