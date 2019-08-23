#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

if __name__ == '__main__':
    source = {0: 'once', 1: 'twice', 2: 'twice'}
    result = dict()

    for key, value in source.items():
        if value not in result.values():
            result[key] = value

    print(json.dumps(result, indent=2))
