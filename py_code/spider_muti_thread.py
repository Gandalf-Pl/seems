# -*- coding: utf-8 -*-

import threading
import requests
import Queue

from HTMLParser import HTMLParser
from urlparse import urljoin, urldefrag

base_url = 'http://www.tornadoweb.org/en/stable/'
concurrency = 10


def get_links_from_url(url):
    response = requests.get(url)
    html = response.content if isinstance(response.content, str) \
        else response.content.decode()
    urls = [urljoin(url, remove_fragment(new_url))
            for new_url in get_links(html)]
    return urls


def remove_fragment(url):
    pure_url, frag = urldefrag(url)
    return pure_url


def get_links(html):
    class URLSeeker(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.urls = []

        def handle_starttag(self, tag, attrs):
            href = dict(attrs).get('href')
            if href and tag == 'a':
                self.urls.append(href)

    url_seeker = URLSeeker()
    url_seeker.feed(html)
    return url_seeker.urls


class UrlThread(threading.Thread):

    def __init__(self, queue, fetched, fetching, name):
        super(UrlThread, self).__init__()
        self.queue = queue
        self.fetched = fetched
        self.fetching = fetching
        self.name = "thread" + str(name)

    def run(self):
        while True:
            url = self.queue.get()
            if url in self.fetching:
                continue
            try:
                self.fetching.add(url)
                print "thread name is {}, fetching url is {}".\
                    format(self.name, url)
                urls = get_links_from_url(url)
                self.fetched.add(url)
                for next_url in urls:
                    if next_url.startswith(base_url) and \
                            next_url not in self.fetched:
                        self.queue.put(next_url)
            except Exception as e:
                print "get exception when fetching url {}, error msg is {}".\
                    format(url, e)
            finally:
                self.queue.task_done()


def main():
    queue = Queue.Queue()
    fetched = set()
    fetching = set()

    # 创建一个线程池
    threads = [UrlThread(queue, fetched, fetching, i)
               for i in xrange(concurrency)]
    for t in threads:
        t.daemon = True
        t.start()
    queue.put(base_url)
    queue.join()


if __name__ == "__main__":
    import time
    start = time.time()
    main()
    print "cost time with multi thread is {}".format(time.time() - start)
