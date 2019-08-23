#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import socket
import threading
import http.server
import argparse
import json

url = False
instance_id = None

schema = {
    "reply": "pong"
}


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

        self.wfile.write(bytes(json.dumps(message, indent=4) + '\n', 'utf8'))


class Thread(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.i = i
        self.daemon = True
        self.start()

    def run(self):
        httpd = http.server.HTTPServer(address, Handler, False)

        httpd.socket = sock
        httpd.server_bind = self.server_close = lambda self: None

        httpd.serve_forever()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', dest="ip", default='0.0.0.0', help='ip address (default: 0.0.0.0)', action="store")
    parser.add_argument('--port', dest="port", default=8000, help='port (default: 8000)', action="store")
    parser.add_argument('--url', dest="url", default=False, help='return url', action='store_true')
    parser.add_argument('--id', dest="id", default=None, help='set return id', action='store')

    args = parser.parse_args()
    url = args.url
    instance_id = args.id

    address = (args.ip, args.port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(3)

    [Thread(i) for i in range(3)]

    print('Started')

    while True:
        time.sleep(9999)
