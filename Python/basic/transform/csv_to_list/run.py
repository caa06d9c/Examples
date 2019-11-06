#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextlib import closing
from csv import reader

if __name__ == '__main__':

    with closing(open('file.csv', 'r')) as csv_file:
        reader_orig = reader(csv_file, delimiter=',')
        for row in reader_orig:
            row_set = [row[0], row[1], row[2], row[3], row[4]]
            print(row_set)
