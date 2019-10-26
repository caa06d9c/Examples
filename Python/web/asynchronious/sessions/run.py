#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aiohttp import web
from aiohttp_session import setup, get_session
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from argparse import ArgumentParser
from base64 import urlsafe_b64decode
from cryptography.fernet import Fernet
from datetime import datetime as dt


routes = web.RouteTableDef()


@routes.get('/')
async def get_handler(request):
    session = await get_session(request)
    last_visit = session['last_visit'] if 'last_visit' in session else 'None'
    text = 'Last visited: {}'.format(last_visit)
    session['last_visit'] = dt.utcnow().isoformat()
    return web.Response(text=text)


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--ip', dest="ip", default='0.0.0.0', help='ip address (default: 0.0.0.0)', action="store")
    parser.add_argument('--port', dest="port", default=80, help='port (default: 80)', action="store")
    parser.add_argument('--cookie_lifetime', dest='cookie_lifetime', default=24, help='lifetime in hours',
                        action="store")

    args = parser.parse_args()

    cookie_lifetime = int(args.cookie_lifetime)

    app = web.Application()
    app.add_routes(routes)

    secret_key = urlsafe_b64decode(Fernet.generate_key())
    setup(app, EncryptedCookieStorage(secret_key))

    web.run_app(app, host=args.ip, port=args.port)
