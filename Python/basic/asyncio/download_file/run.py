#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aiofile import AIOFile
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
        print(f'Scraping {url} failed due to the connection problem')
        return False

    if response.status not in http_ok:
        print(f'Scraping {url} failed due to the return code {response.status}')
        return False

    async with AIOFile(f"{url.rsplit('/', 2)[1]}.json", 'w') as fl:
        await fl.write(dumps(content, indent=4))

    return content


if __name__ == '__main__':
    urls = ['http://demin.co/echo1/', 'http://demin.co/echo2/']

    res = run(scrape(urls))
    print(dumps(res, indent=4))
