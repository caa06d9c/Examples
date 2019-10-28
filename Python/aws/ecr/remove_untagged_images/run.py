#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from boto3 import client
from json import dumps


if __name__ == '__main__':

    registry = ''
    repository = ''

    ecr = client('ecr')
    images = ecr.list_images(registryId=registry,
                             repositoryName=repository,
                             filter={'tagStatus': 'UNTAGGED'})

    for image in images['imageIds']:
        res = ecr.batch_delete_image(registryId = registry,
                                     repositoryName = repository,
                                     imageIds = [{'imageDigest': image['imageDigest']}])
        print(dumps({'image': image['imageDigest'], 'status':  res['ResponseMetadata']['HTTPStatusCode']}, indent=4))
