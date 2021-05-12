#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from asyncio import ensure_future, gather, run
from datetime import  datetime, timedelta
from hashlib import sha512
from random import randint
from uuid import uuid4


async def calc(ct, et):
    et = datetime.utcnow() + timedelta(seconds=et)

    for i in range(0, ct):
        await gather(*[ensure_future(calc_one(et))])


async def calc_one(et):
    while et > datetime.utcnow():
        if randint(0, 100000) < 1:
            print(sha512(str(uuid4()).encode()).hexdigest())
        else:
            sha512(str(uuid4()).encode()).hexdigest()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-c', default=5, help='amount of async streams (complexity)', action='store')
    parser.add_argument('-e', default=-1, help='exit with exit code (-1 means random)', action='store')
    parser.add_argument('-t', default=30, help='seconds before exit', action='store')

    args = parser.parse_args()

    run(calc(args.c, args.t))

    exit(args.e if args.e != -1 else randint(0, 255))
