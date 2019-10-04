#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextlib import closing
from csv import reader
from xlsxwriter import Workbook

if __name__ == '__main__':

    # file1
    workbook = Workbook('file1.xlsx')
    page1 = workbook.add_worksheet()

    with closing(open('file1.csv', 'r')) as csv_file:
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

    # file2
    workbook = Workbook('file2.xlsx')
    page1 = workbook.add_worksheet()

    with closing(open('file2.csv', 'r')) as csv_file:
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
    workbook = Workbook('file3.xlsx')
    page1 = workbook.add_worksheet()

    with closing(open('file3.csv', 'r')) as csv_file:
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