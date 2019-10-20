#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://projecteuler.info/problem=12
# 76576500

from math import ceil
from lib import get_primes, get_devides

if __name__ == '__main__':

    n = 1
    limit = 500
    number = int((n + 1)*n*(1/2))

    primes = get_primes(100000)

    while True:
        count = get_devides(number, primes)

        if count > limit:
            break

        n += 1
        number += n

    print(number)
