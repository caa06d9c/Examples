#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
1,1@ex.com
2,2@ex.com
3,3@ex.com
4,4@ex.com
"""

from argparse import ArgumentParser
from csv import reader, writer
from shutil import copyfile
import os

user = '3@ex.com'
result = 'result.csv'
source = 'file.csv'

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--clean', action='store_true')
    args = parser.parse_args()

    if os.path.isfile(result):
        os.remove(result)

    if args.clean:
        exit(0)

    copyfile(source, result)

    with open(result, 'r+') as csv_file:
        reader_orig = reader(csv_file, delimiter=',')
        in_mem_csv = [row for row in reader_orig if row[1] != user]
        csv_file.truncate(0)

    with open(result, 'w') as csv_file:
        out = writer(csv_file, delimiter=',')
        out.writerows(in_mem_csv)

    csv_file.close()
