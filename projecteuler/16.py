#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://projecteuler.info/problem=15
# 1366

from math import pow

if __name__ == '__main__':

    number = str(int(pow(2, 1000)))
    res = 0
    for el in number:
        res += int(el)

    print(res)
