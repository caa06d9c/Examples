#!/usr/bin/python3
# -*- coding: utf-8 -*-

from asyncio import ensure_future, gather, run
from json import dumps


async def calculate(data):
    tasks = list()
    result = dict()
    temp = None

    for df in data:
        task = ensure_future(calculate_one(df, data[df]))
        tasks.append(task)

        temp = await gather(*tasks)

    for element in temp:
        result[element['df']] = element['ds']

    return result


async def calculate_one(df, dataset):
    result = dict()
    result['df'] = df
    result['ds'] = list()
    for element in dataset:
        result['ds'].append(element + '-processed')

    return result


if __name__ == '__main__':

    src_data = {'df1': ['a1', 'b1', 'c1', 'd1'],
                'df2': ['a2', 'b2', 'c2', 'd2']}

    res = run(calculate(src_data))

    print(dumps(res, indent=4))
