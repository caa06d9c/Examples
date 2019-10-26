#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

txt = "I need to extract UP-3415 from this string"


if __name__ == '__main__':
    print(re.findall('UP-[0-9]{4}', txt)[0])