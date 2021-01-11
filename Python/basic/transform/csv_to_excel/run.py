#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://stackoverflow.com/questions/58240516/import-csv-files-into-excel-files/58244299#58244299

from argparse import ArgumentParser
from contextlib import closing
from csv import reader
from xlsxwriter import Workbook
from shutil import rmtree
import os

store_path = 'files'
sources = 'sources'

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--clean', action='store_true')
    args = parser.parse_args()

    if args.clean:
        if os.path.isdir(store_path):
            rmtree(store_path)
        exit(0)

    if not os.path.isdir(store_path):
        os.makedirs(store_path)

    workbook = Workbook(f"{store_path}/file1.xlsx")
    page1 = workbook.add_worksheet()

    with closing(open(f"{sources}/file1.csv", 'r', encoding='utf8')) as csv_file:
        reader_orig = reader(csv_file, delimiter=' ')
        row = 0
        for el in reader_orig:
            res = dict()
            res['date'] = el[0]
            res['time'] = el[1]
            res['c1'] = el[3]
            res['c2'] = el[4]
            res['c3'] = el[5]
            res['c4'] = el[6]

            col = 0
            for item in res:
                page1.write(row, col, res[item])
                col += 1

            row += 1

    workbook.close()

    # file2
    workbook = Workbook(f"{store_path}/file2.xlsx")
    page1 = workbook.add_worksheet()

    with closing(open(f"{sources}/file2.csv", 'r')) as csv_file:
        reader_orig = reader(csv_file, delimiter=' ')
        row = 0
        for el in reader_orig:
            res = dict()
            res['date'] = el[0]
            res['time'] = el[1]
            res['c1'] = el[3].split(',')[0]
            res['c2'] = el[3].split(',')[1]

            col = 0
            for item in res:
                page1.write(row, col, res[item])
                col += 1

            row += 1

    workbook.close()

    # file3
    workbook = Workbook(f"{store_path}/file3.xlsx")
    page1 = workbook.add_worksheet()

    with closing(open(f"{sources}/file3.csv", 'r')) as csv_file:
        reader_orig = reader(csv_file, delimiter=',')
        row = 0
        for el in reader_orig:
            res = dict()
            res['date'] = el[0].split(' ')[0]
            res['time'] = el[0].split(' ')[1]
            res['c1'] = el[1]
            res['c2'] = el[2]
            res['c3'] = el[3]
            res['c4'] = el[4]
            res['c5'] = el[5]
            res['c6'] = el[6]

            col = 0
            for item in res:
                page1.write(row, col, res[item])
                col += 1

            row += 1

    workbook.close()
