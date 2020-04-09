#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aiofile import AIOFile
from aiohttp import ClientSession
from asyncio import ensure_future, gather, run, Semaphore
from calendar import monthlen

http_ok = [200]
limit = 5
base_url = 'http://datafeed.dukascopy.com/datafeed/{}/{}/{}/{}/{}h_ticks.bi5'


async def download():
    tasks = list()
    sem = Semaphore(limit)

    async with ClientSession() as session:
        for pair in ['AUDUSD']:
            for year in [2014, 2015]:
                for month in range(1, 12):
                    for day in range(1, monthlen(year, month)):
                        for hour in range(0, 23):
                            tasks.append(ensure_future(download_one(pair=pair,
                                                                    year=str(year).zfill(2),
                                                                    month=str(month).zfill(2),
                                                                    day=str(day).zfill(2),
                                                                    hour=str(hour).zfill(2),
                                                                    session=session,
                                                                    sem=sem)))
        return await gather(*tasks)


async def download_one(pair, year, month, day, hour, session, sem):
    url = base_url.format(pair, year, month, day, hour)
    async with sem:
        async with session.get(url) as response:
            content = await response.read()

        if response.status not in http_ok:
            print(f'Scraping {url} failed due to the return code {response.status}')
            return

        try:
            content = content.decode('UTF-8')
        except (UnicodeDecodeError):
            print(f'Dumping {url} failed due to the incorrect content')
            return

        if content != '':
            async with AIOFile(f'{pair}-{year}-{month}-{day}-{hour}.bi5', 'w') as fl:
                await fl.write(content)
        else:
            print(f'Dumping {url} failed due to the empty content')
            return

        return


if __name__ == '__main__':
    run(download())
