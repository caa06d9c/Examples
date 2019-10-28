#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ssl import create_default_context
from socket import socket
from json import dumps

if __name__ == "__main__":
    site = ''

    context = create_default_context()
    conn = context.wrap_socket(socket(), server_hostname=site)
    conn.connect((site, 443))
    cert = conn.getpeercert()

    print(dumps(cert, indent=2))
