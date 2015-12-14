# -*- coding: utf-8 -*-

from redis.sentinel import Sentinel

import time

sentinel = Sentinel([('10.0.10.2', 5002),
                     ('10.0.0.3', 5003),
                     ('10.0.10.4', 5003)], socket_timeout=0.1)

master = sentinel.discover_master("mymaster")

slaves = sentinel.discover_slaves("mymaster")


print master, slaves

redis_master = sentinel.master_for("mymaster", socket_timeout=1)

print "redis_master id is {}".format(id(redis_master))

redis_slave = sentinel.slave_for("mymaster", socket_timeout=1)

# redis_master.hmset("test_set", {"name": "seems", "pwd": "123"})

# print redis_slave.hmget("test_set", ["name", "pwd"])

# data = redis_slave.hgetall("test_set")

# redis_master.hmset("test_copy", data)

# print redis_slave.hgetall("test_copy")

# redis_master.delete("test_add_set")
#
# redis_master.sadd("test_add_set", 1,2,3,4,5,56)
#
# redis_master.sadd("test_def", *list(redis_master.smembers("test_add_set")))
redis_master.sadd("test_abc", *[])
