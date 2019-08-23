#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import contextlib
import csv

if __name__ == '__main__':

    with contextlib.closing(open('file.csv', 'r')) as csv_file:
        reader_orig = csv.reader(csv_file, delimiter=',')
        for row in reader_orig:
            row_set = [row[0], row[1], row[2], row[3], row[4]]
            print(row_set)
