#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://projecteuler.info/problem=3
# 6857

from lib import get_primes
from math import sqrt, ceil

if __name__ == '__main__':
    number = 600851475143
    primes = get_primes(ceil(sqrt(number)))

    for el in range(len(primes) - 1, 0, -1):
        if number % primes[el] == 0:
            print(primes[el])
            exit(0)

    exit(1)
