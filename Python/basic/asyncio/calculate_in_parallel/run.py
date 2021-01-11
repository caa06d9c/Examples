#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://stackoverflow.com/questions/55224511/multiprocess-process-python3-return-dataframes/55226262#55226262
# https://stackoverflow.com/questions/55172403/python-multiprocessing-each-process-returns-list/55173275#55173275

from asyncio import ensure_future, gather, run
from yajl import dumps

data = dict(df1=['a1',
                 'b1',
                 'c1',
                 'd1'],
            df2=['a2',
                 'b2',
                 'c2',
                 'd2'])


async def calculate():
    result = dict()

    for e in await gather(*[ensure_future(calculate_one(k, v)) for k, v in data.items()]):
        result[e['k']] = e['v']

    return result


async def calculate_one(k, v):
    return dict(k=k,
                v=[f"{e}-processed" for e in v])


if __name__ == '__main__':
    print(dumps(run(calculate()), indent=4))
