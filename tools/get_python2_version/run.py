#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE

if __name__ == '__main__':

    cmd = '/usr/local/bin/python2'
    param = '-V'

    command = 'ls -l'
    process = Popen([cmd, param], stdout=PIPE, stderr=PIPE)

    process.wait()
    err, out = process.communicate()

    print(out)
