#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://projecteuler.info/problem=9
# 31875000

if __name__ == '__main__':

    # dirty hack
    # for a in range(1, 1000):
    #     for b in range(1, 1000 - a):
    #         c = 1000 - a - b
    #         if a * a + b * b == c * c:
    #             print(a * b * c)
    #             exit(0)

    for m in range(2, 1000):
        for n in range(1, m):
            if (m - n) % 2 != 0:
                a = n
                b = m
                while a != 0 and b != 0:
                    if a > b:
                        a = a % b
                    else:
                        b = b % a
                if a + b == 1:
                    for k in range(1, 30):
                        a = k * (m * m - n * n)
                        b = k * (2 * m * n)
                        c = k * (m * m + n * n)

                        if a + b + c == 1000:
                            print(a * b * c)
                            exit(0)

    exit(1)
