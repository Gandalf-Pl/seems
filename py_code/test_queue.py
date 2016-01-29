# -*- coding: utf-8 -*-

import Queue
import threading
import time


class WorkerThread(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        print 'In Worker Class'
        while True:
            counter = self.queue.get()
            print 'Going to Sleep'
            time.sleep(counter)
            print ' I am up!'
            self.queue.task_done()
queue = Queue.Queue()

for i in range(10):
    worker = WorkerThread(queue)
    print 'Going to Thread!'
    worker.daemon = True
    worker.start()
for j in range(10):
    queue.put(j)
queue.join()
