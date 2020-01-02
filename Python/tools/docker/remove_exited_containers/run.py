#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from docker import Client

if __name__ == '__main__':
    client = Client(base_url='unix://var/run/docker.sock')
    [client.remove_container(item['Id']) for item in client.containers(all='true', filters={'status': 'exited'})]
