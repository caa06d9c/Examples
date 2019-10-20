#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://projecteuler.info/problem=10
# 142913828922

from lib import get_primes

if __name__ == '__main__':
    primes = get_primes(2000000)
    res = 0

    for el in primes:
        res += el

    print(res)
