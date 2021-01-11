#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from yajl import dumps
from contextlib import closing
from csv import reader

if __name__ == '__main__':
    res = dict()
    with closing(open('file.csv', 'r')) as csv_file:
        reader_orig = reader(csv_file, delimiter=';')
        for el in reader_orig:
            res[el[0]] = dict(url=el[1],
                              type=el[2])

    print(dumps(res, indent=2))
