# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from os import listdir
from yaml import dump
from hashlib import sha256


def get_digest(file_path):
    with open(file_path, 'rb') as file:
        return sha256(file.read()).hexdigest()


def check_hash(files, args):
    print('\nChecking hash')

    reply = list()
    status = False

    for file in files['left']:
        fl = dict()

        for side in files:
            fl[side] = get_digest(f"{getattr(args, side)}/{file}")

        if fl['left'] != fl['right']:
            status = True
            reply.append(file)

    if not status:
        print('\nHashes are equal')
    else:
        print('\nDifferent hashes')
        print(dump(reply))


def main():
    parser = ArgumentParser()
    parser.add_argument('--left', required=True, action='store')
    parser.add_argument('--right', required=True, action='store')

    args = parser.parse_args()

    files = dict(left=listdir(args.left),
                 right=listdir(args.right))

    status = uniq_files(files)
    if status:
        exit(0)

    check_hash(files, args)


def uniq_files(files):
    print('\nChecking uniq')

    uniq = dict(left=list(),
                right=list())

    for k, v in files.items():
        opposite = 'right' if k == 'left' else 'left'
        for file in v:
            if file not in files[opposite]:
                uniq[k].append(file)

    status = False

    for k, v in uniq.items():
        if v:
            status = True
            print(f"{k}: \n{dump(v)}")

    if not status:
        print('\nUniq are not found')

    return status


if __name__ == '__main__':
    main()
