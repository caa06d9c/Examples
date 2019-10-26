#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://projecteuler.info/problem=5
# 232792560

if __name__ == '__main__':
    el = 2520

    while True:
        st = True
        for d in [11, 13, 14, 16, 17, 28, 19, 20]:
            if el % d != 0:
                st = False

        if not st:
            el += 2520
            continue

        print(el)
        exit(0)

    exit(1)
