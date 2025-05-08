import redis
from proxypool.exceptions.empty import PoolEmptyException
import sys

sys.path.append(".")
REDIS_CLIENT_VERSION = redis.__version__
IS_REDIS_VERSION_2 = REDIS_CLIENT_VERSION.startswith('2.')


# class RedisClient(object):
#     def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, **kwargs):
#         self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True, **kwargs)
print(IS_REDIS_VERSION_2)
