#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aiohttp import web
from argparse import ArgumentParser
from yajl import dumps, load

routes = web.RouteTableDef()
tag = None


@routes.post('/{tail:.*}')
async def handle(request):
    return web.Response(text=await handler(request), status=201)


@routes.get('/{tail:.*}')
async def handle(request):
    return web.Response(text=await handler(request), status=200)


@routes.put('/{tail:.*}')
async def handle(request):
    return web.Response(text=await handler(request), status=201)


@routes.patch('/{tail:.*}')
async def handle(request):
    return web.Response(text=await handler(request), status=204)


@routes.delete('/{tail:.*}')
async def handle(request):
    return web.Response(text=await handler(request), status=204)


async def handler(request):
    path = request.raw_path
    method = request.method

    reply = {
        'method': method,
        'path': path
    }

    ip = request.headers.get('X-Forwarded-For')
    if ip:
        reply['ip'] = ip

    host = request.headers.get('Host')
    if host is None:
        request.headers.get('X-Forwarded-Host')
    if host:
        reply['host'] = host

    if tag:
        reply['tag'] = tag

    headers = dict()
    for header in ['X-Forwarded-Port',
                   'X-Forwarded-Proto',
                   'X-Forwarded-Agent',
                   'X-Forwarded-Request',
                   'X-Amzn-Trace-Id']:
        result = request.headers.get(header, None)
        if result:
            headers[header] = result

    if len(headers) != 0:
        reply['headers'] = headers

    return dumps(reply, indent=4)


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--ip', default='0.0.0.0', help='ip address (default: 0.0.0.0)', action='store')
    parser.add_argument('--port', default=8080, help='port (default: 8080)', action='store')
    parser.add_argument('--tag', default='', action='store')
    parser.add_argument('--config', action='store_true')

    args = parser.parse_args()

    app = web.Application()
    app.add_routes(routes)

    if args.tag:
        tag = args.tag

    if args.config:
        with open('./config.json') as f:
            tag = load(f)['tag']

    web.run_app(app, host=args.ip, port=args.port)
