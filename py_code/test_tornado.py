# -*- coding: utf-8 -*-

from tornado import gen
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop


@gen.coroutine
def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    raise gen.Return(response.body)


@gen.coroutine
def get_response(url):
    response = yield fetch_coroutine(url)
    print "response is {}".format(response)
    raise gen.Return(None)


@gen.coroutine
def call_task():
    yield gen.Task(get_response, "http://www.example.com")


if __name__ == "__main__":
    # IOLoop.current().run_sync(lambda: get_response("http://www.example.com"))
    IOLoop.current().run_sync(call_task)

    # IOLoop.current().spawn_callback(get_response, "http://www.example.com")
    # IOLoop.instance().start()
