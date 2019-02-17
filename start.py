#!/usr/bin/python -u
# -*- coding: utf-8 -*-
import redis
import os

config = {
  'redis': {
    'host': 'localhost',
    'port': 6379,
    'password': 'password',
    'db': '0'
  }
}

for section in config:
    for key,value in config[section].items():
        env = os.getenv(section.upper() + '_' + key.upper())
        if env:
            print("%s_%s=\"%s\" as %s" % (section.upper(), key.upper(), env, type(value)))
            config[section][key] = type(value)(env)

r = redis.StrictRedis(**config['redis'])
print("[x] Connected to redis")
r.set('test', 'value')
print("[x] wrote test=value")
value = r.get('test')
print("[x] read test=%s" % value)
r.delete('value')
