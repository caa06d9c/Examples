#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from asyncio import ensure_future, gather, run
from datetime import datetime, timedelta
from hashlib import sha512
from random import randint
from uuid import uuid4


async def calc(ct, et, sp):
    et = datetime.utcnow() + timedelta(seconds=et)

    for i in range(0, ct):
        await gather(*[ensure_future(calc_one(et, sp))])


async def calc_one(et, sp):
    t = 0
    while et > datetime.utcnow():
        t += 1
        tmp = sha512(str(uuid4()).encode()).hexdigest()
        if t == sp:
            print(tmp)
            t = 0


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-c', default=5, help='amount of parallel executions (complexity)', action='store')
    parser.add_argument('-e', default=-1, help='exit code (-1 means random)', action='store')
    parser.add_argument('-t', default=30, help='execution time', action='store')
    parser.add_argument('-s', default=300000, help='output speed', action='store')

    args = parser.parse_args()

    run(calc(int(args.c), int(args.t), int(args.s)))

    exit(int(args.e if args.e != -1 else randint(0, 254)))
