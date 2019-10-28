#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from docker import Client

if __name__ == '__main__':
    client = Client(base_url='unix://var/run/docker.sock')
    [client.remove_image(item['Id'], force=True) for item in client.images() if item['RepoTags'] is None]
