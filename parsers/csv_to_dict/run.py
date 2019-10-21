#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from json import dumps
from contextlib import closing
from csv import reader

if __name__ == '__main__':

    res = dict()

    with closing(open('file.csv', 'r')) as csv_file:
        reader_orig = reader(csv_file, delimiter=';')
        for el in reader_orig:
            local_id = el[0]
            res[local_id] = dict()
            res[local_id]['url'] = el[1]
            res[local_id]['type'] = el[2]

    print(dumps(res, indent=2))
