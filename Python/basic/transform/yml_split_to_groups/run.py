#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from json import dumps

if __name__ == '__main__':
    result = dict()
    last_word = ''

    with open('file.yml', 'r+') as file:
        lines = file.readlines()
        for word in filter(None, (line.rstrip('\n') for line in lines)):
            if word.startswith('['):
                last_word = word[1:-1]
                result[last_word] = list()
            else:
                result[last_word].append(word)

    print(dumps(result, indent=2))
