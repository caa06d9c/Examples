#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aiohttp import ClientSession, client_exceptions
from asyncio import ensure_future, gather, run
from json import dumps, loads

http_ok = [200]


async def scrape(url_list):

    tasks = list()

    async with ClientSession() as session:
        for url in url_list:
            task = ensure_future(scrape_one(url, session))
            tasks.append(task)

        result = await gather(*tasks)

    return result


async def scrape_one(url, session):

    try:
        async with session.get(url) as response:
            content = await response.read()
    except client_exceptions.ClientConnectorError:
        print('Scraping %s failed due to the connection problem', url)
        return False

    if response.status not in http_ok:
        print('Scraping%s failed due to the return code %s', url, response.status)
        return False

    content = loads(content.decode('UTF-8'))

    return content


if __name__ == '__main__':
    urls = ['http://demin.co:8080/echo1/', 'http://demin.co:8080/echo1/']
    res = run(scrape(urls))

    print(dumps(res, indent=4))
