#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1,1@ex.com
2,2@ex.com
3,3@ex.com
4,4@ex.com
"""


import csv

if __name__ == '__main__':

    user = '3@ex.com'

    in_mem_csv = list()
    with open('file.csv', 'r+') as csv_file:
        reader_orig = csv.reader(csv_file, delimiter=',')
        for row in reader_orig:
            if row[1] != user:
                in_mem_csv.append(row)
        csv_file.truncate(0)
        csv_file.close()

    with open('file.csv', 'w') as csv_file:
        out = csv.writer(csv_file, delimiter=',')
        out.writerows(in_mem_csv)
    csv_file.close()
