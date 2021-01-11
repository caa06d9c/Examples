#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from asyncio import ensure_future, gather, run
import os

store_path = 'files'


async def read():
    return await gather(*[ensure_future(read_one(file)) for file in os.listdir(store_path)])


async def read_one(file):
    with open(f"{store_path}/{file}", 'r+') as f:
        return file, [line[:-1] for line in f.readlines()]


if __name__ == '__main__':
    res = run(read())
    for r in res:
        print(f"{r[0]} - {r[1]}")
