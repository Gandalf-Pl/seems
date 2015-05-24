# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345
print >>sys.stderr, "connecting to %s port %s" % (host, port)
s.connect((host, port))

try:
    message = "this is a message, it will be repeated"
    start = raw_input("please input message:")
    print >>sys.stderr, "send %s" % message

    s.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = s.recv(16)
        amount_received += len(data)
        print >>sys.stderr, "received %s" % data

finally:
    print >>sys.stderr, "close socket"
    s.close()

