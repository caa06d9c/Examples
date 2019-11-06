#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
1,1@ex.com
2,2@ex.com
3,3@ex.com
4,4@ex.com
"""

from csv import reader, writer

if __name__ == '__main__':

    user = '3@ex.com'

    with open('file.csv', 'r+') as csv_file:
        reader_orig = reader(csv_file, delimiter=',')
        in_mem_csv = [row for row in reader_orig if row[1] != user]
        csv_file.truncate(0)

    with open('file.csv', 'w') as csv_file:
        out = writer(csv_file, delimiter=',')
        out.writerows(in_mem_csv)
    csv_file.close()
