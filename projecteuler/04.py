#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://projecteuler.info/problem=4
# 906609

if __name__ == '__main__':
    miv = 100
    mav = 1000
    mar = 0

    for a in range(miv, mav):
        for b in range(miv, mav):
            res = str(a * b)
            sz = len(res)

            if sz % 2 != 0:
                continue

            str1 = ''
            str2 = ''

            for i in range(0, int(sz / 2)):
                str1 += res[i]

            for i in range(sz - 1, int(sz / 2) - 1, -1):
                str2 += res[i]

            if str1 == str2:
                if int(res) > mar:
                    mar = int(res)

    print(mar)


