#!/usr/bin/python3
# -*- coding: utf-8 -*-

from asyncio import ensure_future, gather, run
import random

alphabet = 'ABCDEFGH'
size = 5000


async def generate():
    tasks = list()
    result = None

    for el in range(0, size):
        task = ensure_future(generate_one())
        tasks.append(task)

        result = await gather(*tasks)

    return list(set(result))


async def generate_one():
    return ''.join(random.choice(alphabet) for j in range(8))


if __name__ == '__main__':

    my_strings = sorted(run(generate()))

    a = len(my_strings)

    for i in range(1,a):
        if my_strings[i] == my_strings[i-1]:
            exit(1)
    print(str(a))
