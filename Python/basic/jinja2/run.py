#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from jinja2 import Template
from yaml import safe_load as load

if __name__ == '__main__':
    with open('template.j2') as f:
        t = Template(f.read())
    with open('variables.yml') as f:
        v = load(f)

    print(t.render(first=v['first'], second=v['second']))
