#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from asyncio import ensure_future, gather, run
import random

alphabet = 'ABCDEFGH'
size = 500


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

    uniq_my_strings = list(set(my_strings))

    if len(uniq_my_strings) != len(my_strings):
        exit(1)

    for i in range(1, 5):
        print(my_strings[i])

    print("...")
