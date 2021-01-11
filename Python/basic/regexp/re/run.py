#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from re import compile

data = '2.0.81'

if __name__ == '__main__':
    regexp = compile(r"^(\d{1,2}.){2}\d{1,2}(-SNAPSHOT)?$")
    print('valid') if regexp.match(data) else print('not valid')
