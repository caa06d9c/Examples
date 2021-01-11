#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aiobotocore import get_session
from aiobotocore.config import AioConfig
from aiofiles import open as aio_open
from argparse import ArgumentParser
from asyncio import get_event_loop, gather
from botocore import exceptions
from os import mkdir
from shutil import rmtree
from yajl import dumps

storage_path = 'files'
file_name = 'list'


async def main(args):
    session = get_session()
    config = AioConfig(max_pool_connections=args.semaphore)

    with open(file_name) as fl:
        files = [file[:-1] for file in fl.readlines()]

    async with session.create_client('s3',
                                     config=config,
                                     aws_access_key_id=args.key_id,
                                     aws_secret_access_key=args.key) as s3_client:
        async def get(key):
            response = await s3_client.get_object(Bucket=args.bucket,
                                                  Key=key)

            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                async with response['Body'] as stream:
                    data = await stream.read()

                f = await aio_open(storage_path + '/' + key, mode='w')
                await f.write(data.decode('UTF-8'))
                await f.flush()

                return {key: 'Downloaded'}
            else:
                return {key: 'Failed'}

        return await gather(*[get(file) for file in files])


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--bucket', action='store', required=True)
    parser.add_argument('--key', action='store', required=True)
    parser.add_argument('--key_id', action='store', required=True)
    parser.add_argument('--semaphore', action='store', type=int, default=10)

    try:
        rmtree(storage_path, ignore_errors=False, onerror=None)
    except FileNotFoundError:
        pass

    mkdir(storage_path)

    try:
        event_loop = get_event_loop()
        result = event_loop.run_until_complete(main(parser.parse_args()))
        print(dumps(result, indent=2))
    except exceptions.ClientError as e:
        print(e)
