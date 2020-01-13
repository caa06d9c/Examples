#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from boto3 import client
from botocore import exceptions
from yajl import dumps
from argparse import ArgumentParser


def main(args):
    try:
        ecr = client('ecr', region_name=args.region, aws_access_key_id=args.key_id, aws_secret_access_key=args.key)
    except exceptions.ClientError:
        raise

    images = ecr.list_images(registryId=args.registry,
                             repositoryName=args.repository,
                             filter={'tagStatus': 'UNTAGGED'})

    for image in images['imageIds']:
        res = ecr.batch_delete_image(registryId=args.registry,
                                     repositoryName=args.repository,
                                     imageIds=[{'imageDigest': image['imageDigest']}])
        print(dumps({'image': image['imageDigest'], 'status':  res['ResponseMetadata']['HTTPStatusCode']}, indent=4))


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--registry', action='store', required=True)
    parser.add_argument('--repository', action='store', required=True)
    parser.add_argument('--region', action='store', required=True)
    parser.add_argument('--key', action='store', required=True)
    parser.add_argument('--key_id', action='store', required=True)

    main(parser.parse_args())
