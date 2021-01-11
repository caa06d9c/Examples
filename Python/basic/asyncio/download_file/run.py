#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aiofile import AIOFile
from aiohttp import ClientSession, client_exceptions
from argparse import ArgumentParser
from asyncio import ensure_future, gather, run
from shutil import rmtree
import os

http_ok = [200]
store_path = 'files'
files = [dict(name='echo1.json',
              url='http://demin.co/echo1/'),
         dict(name='echo2.json',
              url='http://demin.co/echo2/')]


async def scrape():
    async with ClientSession() as session:
        return await gather(*[ensure_future(scrape_one(url, session)) for url in files])


async def scrape_one(file, session):
    try:
        async with session.get(file['url']) as response:
            content = await response.text()
    except client_exceptions.ClientConnectorError:
        print(f"Scraping {file['url']} failed due to the connection problem")
        return False

    if response.status not in http_ok:
        print(f"Scraping {file['url']} failed due to the return code {response.status}")
        return False

    async with AIOFile(f"{store_path}/{file['name']}", 'w') as fl:
        await fl.write(content)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--clean', action='store_true')
    args = parser.parse_args()

    if args.clean:
        if os.path.isdir(store_path):
            rmtree(store_path)
        exit(0)

    if not os.path.isdir(store_path):
        os.makedirs(store_path)

    run(scrape())
