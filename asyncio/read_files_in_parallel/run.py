#!/usr/bin/python3
# -*- coding: utf-8 -*-

from asyncio import Semaphore, ensure_future, gather, run

limit = 4


async def read(file_list):
    tasks = list()
    result = None

    sem = Semaphore(limit)

    for file in file_list:
        task = ensure_future(read_bounded(file, sem))
        tasks.append(task)

        result = await gather(*tasks)

    return result


async def read_bounded(file, sem):
    async with sem:
        return await read_one(file)


async def read_one(file):

    result = list()
    with open(file, 'r+') as f:
        for line in f.readlines():
            result.append(int(line[:-1]))

    return result


if __name__ == '__main__':
    files = ['1', '2', '3', '4']
    res = run(read(files))

    print(res)
