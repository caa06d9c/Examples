#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aiohttp import ClientSession, client_exceptions
from asyncio import ensure_future, gather, run
from json import dumps, loads

http_ok = [200]


async def scrape(url_list):
    async with ClientSession() as session:
        return await gather(*[ensure_future(scrape_one(url, session)) for url in url_list])


async def scrape_one(url, session):
    try:
        async with session.get(url) as response:
            content = loads(await response.text())
    except client_exceptions.ClientConnectorError:
        print('Scraping %s failed due to the connection problem', url)
        return False

    if response.status not in http_ok:
        print('Scraping%s failed due to the return code %s', url, response.status)
        return False

    return content


if __name__ == '__main__':
    urls = ['http://demin.co/echo1/', 'http://demin.co/echo2/']

    res = run(scrape(urls))
    print(dumps(res, indent=4))
