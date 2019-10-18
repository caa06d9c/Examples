#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://projecteuler.info/problem=10

if __name__ == '__main__':
    prime = 2
    res = 2
    current = 0

    array = list()
    for i in range(2, 2000000):
        array.append(i)

    size = len(array)

    while True:
        status = False

        for i in range(prime - 2, size, prime):
            array[i] = 0

        for i in range(current, size):
            if array[i] != 0:
                prime = array[i]
                current = i
                status = True
                res += prime
                break

        if not status:
            break

    print(res)
