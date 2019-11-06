#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from json import dumps

if __name__ == '__main__':
    source = {0: 'once', 1: 'twice', 2: 'twice'}
    result = dict()

    for key, value in source.items():
        if value not in result.values():
            result[key] = value

    print(dumps(result, indent=4))
