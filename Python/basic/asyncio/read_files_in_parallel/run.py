#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from asyncio import ensure_future, gather, run


async def read(file_list):
    return await gather(*[ensure_future(read_one(file)) for file in file_list])


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
