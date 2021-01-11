#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://projecteuler.info/problem=2
# 4613732

limit = 4000000
a = 1
b = 2
n = 3

if __name__ == '__main__':
    res = 2
    while n <= limit:
        if n % 2 == 0:
            res += n

        a = b
        b = n
        n = a + b

    print(res)
