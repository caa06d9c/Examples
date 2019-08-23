#!/usr/bin/python3
# -*- coding: utf-8 -*-

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def normalize(string):
    stage1 = "".join(IBAN.split()).upper()
    stage2 = ''
    for l in stage1:
        if l in alphabet:
            stage2 = stage2 + l

    return stage2.split('IBAN')[1]


if __name__ == '__main__':

    IBAN_LIST = ['IBAN NL 91ABNA0417463300', 'IBAN NL91ABNA0417164300', 'Iban: NL 69 ABNA 402032566', '']

    STAGE_1 = list()
    for IBAN in IBAN_LIST:
        IBAN_normalized = normalize(IBAN)
        print(IBAN_normalized[2:4], IBAN_normalized[8:])




