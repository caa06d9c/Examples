#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aiohttp import ClientSession, client_exceptions
from asyncio import ensure_future, gather, run
from yajl import dumps, loads

http_ok = [200]
urls = ['http://demin.co/echo1/',
        'http://demin.co/echo2/']


async def scrape():
    async with ClientSession() as session:
        return await gather(*[ensure_future(scrape_one(url, session)) for url in urls])


async def scrape_one(url, session):
    try:
        async with session.get(url) as response:
            content = await response.text()
    except client_exceptions.ClientConnectorError:
        print(f'Scraping {url} failed due to the connection problem')
        return False

    if response.status not in http_ok:
        print(f'Scraping {url} failed due to the return code {response.status}')
        return False

    return loads(content)


if __name__ == '__main__':
    print(dumps(run(scrape()), indent=4))
