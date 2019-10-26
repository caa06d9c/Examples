#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_primes(last, limit=-1):
    primes = list()
    primes.append(2)
    current = 0

    array = list()
    for i in range(2, last):
        array.append(i)

    size = len(array)

    while True:
        status = False

        for i in range(primes[-1] - 2, size, primes[-1]):
            array[i] = 0

        for i in range(current, size):
            if array[i] != 0:
                primes.append(array[i])
                current = i
                status = True
                break

        if len(primes) == limit:
            return primes

        if not status:
            break

    return primes


def get_devides(number, primes):
    array = dict()
    res = 1

    if number == 1:
        return 1

    if number in primes:
        return 2

    while number not in primes:
        check = number

        for el in primes:
            if number % el == 0:
                if el not in array:
                    array[el] = 0
                array[el] += 1
                number = int(number / el)
                break

        if check == number:
            print('loop detected, extend the primes range')
            exit(1)

    if number not in array:
        array[number] = 1

    for el in array:
        res *= (array[el] + 1)

    return res
