#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://projecteuler.info/problem=1
# 233168

if __name__ == '__main__':
    print(sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]))
