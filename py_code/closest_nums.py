# -*- coding: utf-8 -*-

from random import randrange
import time


def two_for(seq):
    dd = float("inf")
    for x in seq:
        for y in seq:
            if x == y: continue
            d = abs(x-y)
            if d < dd:
                xx, yy, dd = x, y, d

    return xx, yy, dd


def one_for(seq):
    seq.sort()
    dd = float("inf")
    for i in xrange(len(seq)-1):
        x, y = seq[i], seq[i+1]
        if x == y: continue
        d = abs(x-y)
        if d < dd:
            xx, yy, dd = x, y, d

    return xx, yy, dd

if __name__ == "__main__":
    # 求一个序列中的相差最少的两个数
    # two_for函数非常简单粗暴的对这个序列进行了嵌套循环，
    # 然后进行逐个比较，最后得到相差最少的两个数

    # one_for这个函数为了达到同样的目的，简化了函数的输入
    # 首先对输入的数列进行排序,然后逐个比较相关两个数之间
    # 的差值,通过这样的思考可以分步处理问题,使得问题得到
    # 简化

    # 函数的输出结果显示两个函数的执行效率相差很多

    seq = [randrange(10**10) for i in xrange(10000)]

    t1 = time.time()
    print two_for(seq)
    print "two for cost time is %s " % (time.time() - t1)
    t2 = time.time()
    print one_for(seq)
    print "one for cost time is %s " % (time.time() - t2)
