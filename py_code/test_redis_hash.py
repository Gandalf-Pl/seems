# coding: utf8

import redis

prefix = "django_red_packet"

max_number = 1000


if __name__ == "__main__":
    rd1 = redis.Redis(db=0)
    rd2 = redis.Redis(db=1)
    rd3 = redis.Redis(db=2)
    rd1.set("test", 0)
    rd2.set("test", 0)
    rd3.set("test", 0)

    rds_list = [rd1, rd2, rd3]

    for x in xrange(max_number):
        key = prefix + str(x)
        hash_key = hash(key) % 3
        conn = rds_list[hash_key]
        conn.incr("test", 1)

    print rd1.get("test")

    print rd2.get("test")

    print rd3.get("test")
