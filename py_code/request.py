# -*- coding: utf-8 -*-

from twisted.internet import reactor
from twisted.internet.defer import Deferred, succeed
from twisted.internet.protocol import Protocol
from twisted.web.client import Agent
from twisted.web.iweb import IBodyProducer
from twisted.web.http_headers import Headers

from zope.interface import implements

import urllib


class StringProducer(object):
    implements(IBodyProducer)

    def __init__(self, body):
        self.body = body
        self.length = len(body)

    def startProducing(self, consumer):
        consumer.write(self.body)
        return succeed(None)

    def pauseProducing(self):
        pass

    def stopProducing(self):
        pass


class BeginningPrinter(Protocol):
    def __init__(self, finished):
        self.finished = finished
        self.buf = ""

    def dataReceived(self, data):
        self.buf += data

    def connectionLost(self, reason):
        print 'Finished receiving body:', reason.getErrorMessage()
        self.finished.callback(self.buf)


def httpRequest(url, method="GET", values=None, headers=None, timeout=3):
    """
    发送http请求
    :param url:
    :param method:
    :param values:
    :param headers:
    :param timeout:
    :return:
    """
    if not headers:
        headers = {}
    if not values:
        values = {}
    data = urllib.urlencode(values)
    agent = Agent(reactor, connectTimeout=timeout)
    d = agent.request(
        method,
        url,
        Headers(headers),
        StringProducer(data) if data else None)

    def handle_response(response):
        d = Deferred()
        response.deliverBody(BeginningPrinter(d))
        return d

    def handle_shutdown(response):
        reactor.stop()

    d.addCallback(handle_response)
    d.addBoth(handle_shutdown)
    reactor.run()

if __name__ == "__main__":
    print httpRequest("http://www.baidu.com/")

