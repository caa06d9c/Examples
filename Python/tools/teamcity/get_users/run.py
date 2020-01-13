#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from yajl import loads, dumps
from argparse import ArgumentParser
from aiohttp import ClientSession, client_exceptions, BasicAuth
from logging import error, getLogger, INFO
from asyncio import ensure_future, gather, run

tc_users = '{}/httpAuth/app/rest/users'
tc_user = tc_users + '/id:{}'
headers = {"accept": "application/json"}
http_ok = [200]


async def users(url, auth):
    async with ClientSession() as session:
        try:
            async with session.get(url, auth=auth, headers=headers) as response:
                content = await response.text()
        except client_exceptions.ClientConnectorError:
            error('users:ClientConnectionError')
            return False

        if response.status not in http_ok:
            error('users:StatusCode:%s', response.status)
            return False

    return content


async def user(user_list, trg_url, trg_auth):
    async with ClientSession() as trg_session:
        async def get(el, url, auth, session):
            try:
                async with session.get(tc_user.format(url, str(el['id'])), auth=auth, headers=headers) as response:
                    if response.status in http_ok:
                        content = await response.text()
            except client_exceptions.ClientConnectorError:
                error('user_one:%s:ClientConnectionError', el['username'])
                return False

            if response.status not in http_ok:
                error('user_one:%s:StatusCode:%s', el['username'], response.status)
                return False

            return loads(content)

        return await gather(*[get(usr, trg_url, trg_auth, trg_session) for usr in user_list])


def main(args):
    auth = BasicAuth(login=args.username, password=args.password)
    user_list = list()

    result = run(users(tc_users.format(args.url), auth))
    if not result:
        exit(1)
    result = loads(result)

    [user_list.append(el) for el in result['user']]

    print(dumps(run(user(user_list, args.url, auth)), indent=2))


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--url', action='store', required=True)
    parser.add_argument('--username', action='store', required=True)
    parser.add_argument('--password', action='store', required=True)

    getLogger().setLevel(INFO)

    main(parser.parse_args())
