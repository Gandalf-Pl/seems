# -*- coding: utf-8 -*-

from twisted.internet import reactor, defer


def getDummyData(x):
    """
    return a defer.Deferred
    :param x:
    :return:
    """
    d = defer.Deferred()
    reactor.callLater(2, d.callback, getDouble)
    return d

def getDouble(x):
    return x * 2


def printData(d):
    print d


d = getDummyData(3)

d.addCallback(printData)

reactor.callLater(4, reactor.stop)

reactor.run()
