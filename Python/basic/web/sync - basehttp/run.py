#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading
import http.server
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from argparse import ArgumentParser
from json import dumps

url = False
instance_id = None

schema = {
    "reply": "pong"
}


# noinspection PyPep8Naming
class Handler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'application/json')
        self.end_headers()

        message = schema.copy()

        if url:
            message['url'] = self.requestline.split('HTTP')[0].strip()

        if instance_id:
            message['id'] = instance_id

        self.wfile.write(bytes(dumps(message, indent=4) + '\n', 'utf8'))


# noinspection PyShadowingNames
class Thread(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.i = i
        self.daemon = True
        self.start()

    def run(self):
        # noinspection PyArgumentList
        httpd = http.server.HTTPServer(address, Handler, False)

        httpd.socket = sock
        # noinspection PyAttributeOutsideInit
        httpd.server_bind = self.server_close = lambda self: None

        httpd.serve_forever()


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--ip', dest="ip", default='0.0.0.0', help='ip address (default: 0.0.0.0)', action="store")
    parser.add_argument('--port', dest="port", default=80, help='port (default: 80)', action="store")
    parser.add_argument('--url', dest="url", default=False, help='return url', action='store_true')
    parser.add_argument('--id', dest="id", default=None, help='set return id', action='store')

    args = parser.parse_args()
    url = args.url
    instance_id = args.id

    address = (args.ip, args.port)

    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(3)

    [Thread(i) for i in range(3)]

    print('Started')

    while True:
        time.sleep(9999)
