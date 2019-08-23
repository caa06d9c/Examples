#!/usr/bin/python3
# -*- coding: utf-8 -*-

from requests import post, auth, exceptions
from json import loads

if __name__ == '__main__':

    client_id = ''
    client_secret = ''
    user = ''
    password = ''

    access_point = 'https://account.lab.fiware.org/oauth2/token'
    grant_type = 'password'

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    auth = auth.HTTPBasicAuth(client_id, client_secret)

    data = {'grant_type': grant_type,
            'username': user,
            'password': password}

    resp = None
    try:
        resp = post(access_point, auth=auth, data=data, headers=headers, timeout=5)
    except exceptions.ConnectionError:
        exit(1)

    if resp.status_code == 200:
        resp = loads(resp.text)
        if 'access_token' in resp:
            print(resp['access_token'])
            exit(0)

    exit(1)
