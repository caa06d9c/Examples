#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aiohttp import web
from argparse import ArgumentParser
from base64 import urlsafe_b64encode, urlsafe_b64decode
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from datetime import datetime as dt
from yajl import dumps, loads


cipher_suite = None
cookie_name = 'ASYNC-Cookie'
http_ok = [200, 201, 204]
routes = web.RouteTableDef()


@routes.get('/')
async def get_handler(request):
    cookie = request.cookies.get(cookie_name)
    last_visit = 'None'

    if cookie is not None:
        cookie = loads(cipher_suite.decrypt(urlsafe_b64decode(cookie)).decode('UTF-8'))
        last_visit = cookie['last_visit']

    text = 'Last visited: {}'.format(last_visit)

    cookie = dict()
    cookie['last_visit'] = dt.utcnow().isoformat()

    cookie = urlsafe_b64encode(cipher_suite.encrypt(dumps(cookie).encode())).decode('UTF-8')

    response = web.Response(text=text)
    response.set_cookie(name=cookie_name,
                        value=cookie)

    return response


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--ip', dest="ip", default='0.0.0.0', help='ip address (default: 0.0.0.0)', action="store")
    parser.add_argument('--port', dest="port", default=80, help='port (default: 80)', action="store")
    parser.add_argument('--cookie_key', dest='cookie_key', default='sdjkf2i3u2fd', help='password to encrypt cookie',
                        action="store")
    parser.add_argument('--cookie_lifetime', dest='cookie_lifetime', default=24, help='lifetime in hours',
                        action="store")

    args = parser.parse_args()

    cookie_lifetime = int(args.cookie_lifetime)

    app = web.Application()
    app.add_routes(routes)

    salt = b'dfvuy3947r397gfbcvdfvaofp398434'

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    cipher_suite = Fernet(urlsafe_b64encode(kdf.derive(args.cookie_key.encode())))

    web.run_app(app, host=args.ip, port=args.port)
