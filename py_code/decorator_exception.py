# -*- coding: utf-8 -*-

import functools


def test_decorator(func):
    """
    测试decorator的异常处理
    """

    @functools.wraps(func)
    def _inner(*args, **kwargs):
        res = func(*args, **kwargs)
        return res

    return _inner


def test_catch_exception_decorator(func):
    """
    test catch exception in decorator
    """

    @functools.wraps(func)
    def _inner(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            print "args is {}".format(*args)
            return res
        except Exception as e:
            print e.message
            # raise e

    return _inner


@test_decorator
def test_raise_exception():
    """"""
    raise Exception("test raise error")


@test_decorator
def test_normal():
    """"""
    return "ok"


@test_catch_exception_decorator
def test_catch_exception(*args):
    raise Exception("test raise error in function")


if __name__ == "__main__":
    print test_normal()
    print test_catch_exception('test1', "test2")
    # print test_raise_exception()
