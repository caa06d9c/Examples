#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://stackoverflow.com/questions/55210627/regex-for-iban-mask/55210903#55210903

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
ibans = ['IBAN NL 91ABNA0417463300',
         'IBAN NL91ABNA0417164300',
         'Iban: NL 69 ABNA 4020325616']


def normalize(item):
    stage1 = "".join(item.split()).upper()
    stage2 = ''
    for item in stage1:
        if item in alphabet:
            stage2 = stage2 + item

    return stage2.split('IBAN')[1]


if __name__ == '__main__':
    print('\n'.join('{} {}'.format(i[2:4], i[8:]) for i in [normalize(iban) for iban in ibans]))
