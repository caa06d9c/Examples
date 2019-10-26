#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://projecteuler.info/problem=6
# 25164150

if __name__ == '__main__':
    res1 = 0
    res2 = 0

    for el in range(1, 101):
        res1 += el * el
        res2 += el

    print(res2 * res2 - res1)
