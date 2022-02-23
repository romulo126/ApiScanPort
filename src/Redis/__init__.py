import redis
import os

port_redis = os.getenv('PORT_REDIS')
password_redis = os.getenv('PASSWORD_REDIS')

r = redis.Redis(
    host='redis',
    port=int(port_redis),
    password=password_redis)

def set_value(key, value):
    r.lpush(key,value)

def remove_value(key, value):
    r.lrem(key, 0, value)

def get_value(key):
    return r.lrange(key, 0, -1)