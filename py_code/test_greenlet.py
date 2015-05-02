# coding: utf8
from greenlet import greenlet


def test1():
    print "12"
    gr2.switch()
    # After print 34, the gr1 dies,
    print "34"


def test2():
    print "56"
    gr1.switch()
    print "78"

# Remember, switches are not calls, but transfer of execution between
# parallel “stack containers”, and the “parent” defines which stack
# logically comes “below” the current one.
gr1 = greenlet(test1)
gr2 = greenlet(test2)
# gr1.getcurrent() 获取当前的greenlet
# gr1.GreenletExit() 退出当天的greentlet
gr1.switch()