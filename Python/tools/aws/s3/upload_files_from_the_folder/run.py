#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aiobotocore import get_session
from aiobotocore.config import AioConfig
from aiofiles import open as aio_open
from argparse import ArgumentParser
from asyncio import get_event_loop, gather
from botocore import exceptions
from os import path, listdir
from yajl import dumps


storage_path = 'files'


async def main(loop, args):
    session = get_session(loop=loop)
    config = AioConfig(max_pool_connections=args.semaphore)
    home = path.dirname(path.realpath(__file__))

    keys = listdir('./files/')
    paths = [home + '/files/' + keys[i] for i in range(0, len(keys))]

    async with session.create_client('s3',
                                     config=config,
                                     aws_access_key_id=args.key_id,
                                     aws_secret_access_key=args.key) as s3_client:
        async def put(key, f_path):
            f = await aio_open(f_path, mode='r')
            fl = await f.read()
            await f.close()

            response = await s3_client.put_object(Bucket=args.bucket,
                                                  Key=key,
                                                  Body=fl)
            if response['ResponseMetadata']['HTTPStatusCode'] != 200:
                return {key: 'Failed'}
            else:
                return {key: 'Uploaded'}

        return await gather(*[put(keys[i], paths[i]) for i in range(0, len(keys))])


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--bucket', action='store', required=True)
    parser.add_argument('--key', action='store', required=True)
    parser.add_argument('--key_id', action='store', required=True)
    parser.add_argument('--semaphore', action='store', type=int, default=10)

    if not path.isdir(storage_path):
        exit(1)

    try:
        event_loop = get_event_loop()
        result = event_loop.run_until_complete(main(event_loop,  parser.parse_args()))
        print(dumps(result, indent=2))
    except exceptions.ClientError as e:
        print(e)
