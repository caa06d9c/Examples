#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://stackoverflow.com/questions/55268350/how-to-make-this-python-script-run-faster/55268666#55268666
# https://stackoverflow.com/questions/55186122/asyncio-aiohttp-not-returning-response/55186376#55186376

from aiohttp import ClientSession, client_exceptions
from asyncio import Semaphore, ensure_future, gather, run
from yajl import dumps, loads

semaphore = 10
http_ok = [200]
urls = ['http://demin.co/echo1/',
        'http://demin.co/echo2/']


async def scrape(url_list):
    sem = Semaphore(semaphore)

    async with ClientSession() as session:
        return await gather(*[ensure_future(scrape_one(url, sem, session)) for url in url_list])


async def scrape_one(url, sem, session):
    async with sem:
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
    print(dumps(run(scrape(urls)), indent=4))
