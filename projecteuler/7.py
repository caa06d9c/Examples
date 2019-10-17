#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://projecteuler.info/problem=7
# stupid way

if __name__ == '__main__':
    primes = list()
    primes.append(2)

    temp = list()
    for i in range(2, 200000):
        temp.append(i)

    while True:
        for i in range(0, len(primes)):
            for j in range(primes[i] - 2, len(temp), primes[i]):
                temp[j] = 0

        for i in range(0, len(temp)):
            if temp[i] != 0:
                primes.append(temp[i])
                break

        if len(primes) == 10001:
            print(primes[10000])
            exit(0)

        if len(list(set(temp))) == 1:
            break

    print(len(primes))
