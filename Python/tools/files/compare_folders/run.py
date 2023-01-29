# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from os import remove, path, walk, rmdir, listdir
from hashlib import sha256


def get_digest(file_path):
    with open(file_path, 'rb') as file:
        return sha256(file.read()).hexdigest()


def main():
    parser = ArgumentParser()
    parser.add_argument('--left', required=True, action='store')
    parser.add_argument('--right', required=True, action='store')
    parser.add_argument('--silent', required=False, action='store_true')

    args = parser.parse_args()

    dirs = dict(left=r'',
                right=r'')

    if not dirs:
        dirs = dict(left=args.left,
                    right=args.right)
    objects = dict(left=[it for sl in [[path.join(i[0], j) for j in i[2]] for i in walk(dirs['left'])] for it in sl],
                   right=[it for sl in [[path.join(i[0], j) for j in i[2]] for i in walk(dirs['right'])] for it in sl])

    for s in ['left', 'right']:
        for f in range(len(objects[s])):
            objects[s][f] = objects[s][f].replace(dirs[s], '')

    uniq_left = list()
    uniq_right = list()
    shared = list()

    for item in objects['left']:
        if item in objects['right']:
            shared.append(item)
        else:
            uniq_left.append(item)

    for item in objects['right']:
        if item not in objects['left']:
            uniq_right.append(item)

    if uniq_left:
        print(f'uniq left: {len(uniq_left)}')

    if uniq_right:
        print(f'uniq right: {len(uniq_right)}')

    if shared:
        print(f'shared: {len(shared)}')
        print(f'\nChecking shared')

        identical = list()
        different = list()

        for item in shared:
            if get_digest(f"{dirs['left']}/{item}") == get_digest(f"{dirs['right']}/{item}"):
                identical.append(item)
            else:
                different.append(item)

        print(f'\nidentical: {len(identical)}')
        print(f'different: {len(different)}')

        if len(identical) > 0:
            if not args.silent:
                if input('Delete?(y/n)') != 'y':
                    print('\nExiting')
                    exit()

            print('\nDeleting')
            for file in identical:
                remove(f"{dirs['right']}{file}")

            dirs_to_delete = list()
            for pth, dirs, files in walk(dirs['right']):
                dirs_to_delete.append(pth)

            dirs_to_delete.reverse()
            for d in dirs_to_delete:
                if len(listdir(d)) == 0:
                    rmdir(d)


if __name__ == '__main__':
    main()
