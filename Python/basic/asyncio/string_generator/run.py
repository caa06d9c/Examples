#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://stackoverflow.com/questions/55184474/python-multiple-processes-consuming-iterating-over-single-generator-divide-and/55184907#55184907

from asyncio import ensure_future, gather, run
from random import choice

alphabet = 'ABCDEFGH'
size = 10


async def generate():
    return list(set(await gather(*[ensure_future(generate_one()) for _ in range(0, size)])))


async def generate_one():
    return ''.join(choice(alphabet) for _ in range(8))


if __name__ == '__main__':
    my_strings = sorted(run(generate()))
    uniq_my_strings = list(set(my_strings))

    if len(uniq_my_strings) != len(my_strings):
        exit(1)

    print('\n'.join('{}'.format(i) for i in my_strings))
