#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://projecteuler.info/problem=2
# 4613732

if __name__ == '__main__':
    limit = 4000000
    res = 2

    a = 1
    b = 2
    n = 3

    while n <= limit:
        if n % 2 == 0:
            res += n

        a = b
        b = n
        n = a + b

    print(res)
