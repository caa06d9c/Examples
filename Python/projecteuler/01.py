#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://projecteuler.info/problem=1
# 233168

if __name__ == '__main__':
    limit = 1000
    a = 3
    b = 5
    res = 0

    for el in range(1, limit):
        if el % a == 0:
            res += el
        elif el % b == 0:
            res += el

    print(res)
