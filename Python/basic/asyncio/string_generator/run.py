#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from asyncio import ensure_future, gather, run
from random import choice

alphabet = 'ABCDEFGH'
size = 500


async def generate():
    return list(set(await gather(*[ensure_future(generate_one()) for _ in range(0, size)])))


async def generate_one():
    return ''.join(choice(alphabet) for _ in range(8))


if __name__ == '__main__':

    my_strings = sorted(run(generate()))
    uniq_my_strings = list(set(my_strings))

    if len(uniq_my_strings) != len(my_strings):
        exit(1)

    for i in range(1, 5):
        print(my_strings[i])

    print("...")
