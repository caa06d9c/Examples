#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://projecteuler.info/problem=15
# 137846528820

from math import factorial, pow

if __name__ == '__main__':
    size = 20
    moves = factorial(size * 2)/pow(factorial(size), 2)
    print(int(moves))
