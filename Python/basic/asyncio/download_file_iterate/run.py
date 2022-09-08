#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://stackoverflow.com/questions/61105464/how-to-download-multiple-files-using-asyncio-and-wget-in-python/61129896#61129896

from aiofile import AIOFile
from aiohttp import ClientSession
from argparse import ArgumentParser
from asyncio import ensure_future, gather, run, Semaphore
from calendar import Calendar
from lzma import open as lzma_open
from shutil import rmtree
from struct import calcsize, unpack
from io import BytesIO
from yajl import dumps
import os

fmt = '>3i2f'
chunk_size = calcsize(fmt)
http_ok = [200]
store_path = 'files'
semaphore = 10
years = [2014,
         2015]
pairs = ['AUDUSD']
url_template = 'http://datafeed.dukascopy.com/datafeed/{}/{}/{}/{}/{}h_ticks.bi5'


async def download():
    tasks = list()
    sem = Semaphore(semaphore)

    async with ClientSession() as session:
        for pair in pairs:
            for year in years:
                for month in range(1, 12):
                    for day in Calendar().itermonthdates(year=year,
                                                         month=month):
                        if day.year != year:
                            continue

                        for hour in range(0, 23):
                            tasks.append(ensure_future(download_one(pair=pair,
                                                                    year=str(year).zfill(2),
                                                                    month=str(month).zfill(2),
                                                                    day=str(day.day).zfill(2),
                                                                    hour=str(hour).zfill(2),
                                                                    session=session,
                                                                    sem=sem)))

        return await gather(*tasks)


async def download_one(pair, year, month, day, hour, session, sem):
    url = url_template.format(pair, year, month, day, hour)
    data = list()

    async with sem:
        async with session.get(url) as response:
            content = await response.read()

        if response.status not in http_ok:
            print(f'Scraping {url} failed due to the return code {response.status}')
            return

        if content == b'':
            print(f'Scraping {url} failed due to the empty content')
            return

        print(f'Scraping {url} succeeded')

        with lzma_open(BytesIO(content)) as f:
            while True:
                chunk = f.read(chunk_size)
                if chunk:
                    data.append(unpack(fmt, chunk))
                else:
                    break

        async with AIOFile(f'{store_path}/{pair}-{year}-{month}-{day}-{hour}.bi5', 'w') as fl:
            await fl.write(dumps(data, indent=4))

        return


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

    run(download())
