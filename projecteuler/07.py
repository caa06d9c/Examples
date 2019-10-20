#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://projecteuler.info/problem=7
# 104743

from lib import get_primes

if __name__ == '__main__':
    primes = get_primes(110000, 10001)
    print(primes[-1])
