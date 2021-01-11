#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# https://stackoverflow.com/questions/55150301/geting-version-of-python-executable-from-a-script/55150531#55150531

from subprocess import Popen, PIPE

if __name__ == '__main__':

    cmd = '/usr/local/bin/python2'
    param = '-V'

    command = 'ls -l'
    process = Popen([cmd, param], stdout=PIPE, stderr=PIPE)

    process.wait()
    err, out = process.communicate()

    print(out)
