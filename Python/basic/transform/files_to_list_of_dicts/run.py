#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':

    with open('file.txt', 'r+') as file:
        for line in file.readlines():
            row_set = [row[0], row[1], row[2], row[3], row[4]]
            print(row_set)
