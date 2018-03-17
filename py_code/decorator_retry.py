# -*- coding: utf-8 -*-


def retry(times=3):
    def inner(func):
        def _inner(*args, **kwargs):
            local_times = times
            while local_times > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(e)
                    local_times -= 1
        return _inner
    return inner


@retry(2)
def test_retry():
    print("hello")
    raise Exception("test")


test_retry()
