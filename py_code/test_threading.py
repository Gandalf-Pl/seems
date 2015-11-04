# -*- coding: utf-8 -*-

from threading import Thread


def countdown(n):
    while n > 0:
        n -= 1

COUNT = 10000000


def use_thread(n):
    t1 = Thread(target=countdown, args=(n//2,))
    t2 = Thread(target=countdown, args=(n//2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


class CountdownThread(Thread):

    def __init__(self, count):
        super(CountdownThread, self).__init__()
        self.count = count

    def run(self):
        while self.count > 0:
            self.count -= 1
        return


if __name__ == "__main__":
    import time
    x1 = time.time()
    countdown(COUNT)
    print time.time() - x1

    x2 = time.time()
    threads = []

    for x in xrange(2):
        threads.append(CountdownThread(COUNT//2))

    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print time.time() - x2
