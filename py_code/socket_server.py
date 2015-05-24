# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345

s.bind((host, port))

s.listen(5)

while True:
    print "Waiting for connection"
    connection, client_address = s.accept()
    print "Got connection from address:", client_address
    try:
        while True:
            data = connection.recv(16)
            print >>sys.stderr, "received data is %s" % data
            if data:
                print >>sys.stderr, "sending data back to the client"
                connection.sendall(data)
            else:
                print >>sys.stderr, "no more data from", client_address
                break
    finally:
        # clean up the connection
        connection.close()


