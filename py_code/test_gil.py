# coding: utf8
# Python threads: internals
# • Only one thread can be active in Python interpreter
# • Each ‘running’ thread requires exclusive access to data
# structures in Python interpreter
# • Global interpreter lock (GIL) provides this exclusive
# synchronization
# • This lock is necessary mainly because CPython's
# memory management is not thread-safe.
# • Result
# – A thread waits if another thread is holding the GIL, even on
# a multi-core processor! So, threads run sequentially,
# instead of parallel!


def dead_loop():
    while True:
        pass


import threading

t = threading.Thread(target=dead_loop)

t.start()
dead_loop()

t.join()
