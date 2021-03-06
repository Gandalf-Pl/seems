# coding: utf8
import redis
import multiprocessing

MAX_NUMBER = 500


def incr_key_in_redis():
    """
    redis的incr是原子操作,可以当成一个计数器,在并发情况下能够保证总数的正确
    :return:
    """
    conn = redis.Redis()
    for x in xrange(1000):
        r1 = conn.incr("test", 1)
        if r1 > MAX_NUMBER:
            conn.incr("test", -1)


if __name__ == "__main__":
    # multiprocessing python的多进程
    for i in xrange(5):
        p = multiprocessing.Process(target=incr_key_in_redis)
        p.start()
        # To wait until a process has completed its work and exited,
        # use the join() method. 如果不使用join,其他进程不会等待它结束
        # join可以传递参数,指定它的timeout时间
        p.join()
