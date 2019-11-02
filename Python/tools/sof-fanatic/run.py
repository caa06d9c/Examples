#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
from random import randint as random
from os import environ as env
from sys import stdout
from selenium import webdriver, common
from selenium.webdriver.chrome.options import Options
from subprocess import Popen, PIPE
from argparse import ArgumentParser
from logging import basicConfig, INFO, info


login = 'https://stackoverflow.com/users/login'
logout = 'https://stackoverflow.com/users/logout'
actions = {'user': 'https://stackoverflow.com/users/{}',
           'reputation': 'https://stackoverflow.com/users/{}?tab=reputation',
           'question': 'https://stackoverflow.com/questions/tagged/{}?tab=Newest',
           'bounty': 'https://stackoverflow.com/questions/tagged/{}?tab=Bounties'}


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--min', default=5, type=int, action='store')
    parser.add_argument('--max', default=19, type=int, action='store')
    parser.add_argument('--actions', nargs='+', default='user reputation question', action='store')
    parser.add_argument('--tags', nargs='+', default='python bash', action='store')
    parser.add_argument('--questions', default=2, type=int, action='store')
    parser.add_argument('--vnc', action='store_true')

    args = parser.parse_args()

    basicConfig(stream=stdout, level=INFO)

    cmd_vfb = ['Xvfb', ':0', '-shmem', '-screen', '0', '1024x768x24', '-fbdir', '/var/tmp']

    info('Starting')

    process_vnc = None
    process_vfb = Popen(cmd_vfb, stdout=PIPE, stderr=PIPE)
    sleep(5)

    if args.vnc:
        cmd_vnc = ['x11vnc', '-display', ':0', '-noxrecord', '-noxfixes', '-noxdamage', '-forever', '-passwd',
                   env['VNC_P']]
        process_vnc = Popen(cmd_vnc, stdout=PIPE, stderr=PIPE)
        sleep(5)

    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--user-data-dir=.chromium")
    d = webdriver.Chrome(options=options)

    info('Started')
    d.get(login.format(env['USER_ID']))

    try:
        info('Login')
        el = d.find_element_by_xpath('//*[@id="email"]')
        el.send_keys(env['USERNAME'])

        el = d.find_element_by_xpath('//*[@id="password"]')
        el.send_keys(env['PASSWORD'])

        el = d.find_element_by_xpath('//*[@id="submit-button"]')
        el.click()
    except common.exceptions.NoSuchElementException:
        pass

    sleep(random(args.min, args.max))

    for action in args.actions:
        if action == 'question':
            for tag in args.tags:
                info(tag)

                d.get(actions['question'].format(tag))
                sleep(random(args.min, args.max))

                els = d.find_elements_by_xpath('//*[@class="question-hyperlink"]')
                urls = [els[i].get_attribute("href") for i in range(0, args.questions)]
                for url in urls:
                    d.get(url)
                    sleep(random(args.min, args.max))

                d.get(actions['bounty'].format(tag))
                sleep(random(args.min, args.max))
        else:
            print(action)
            d.get(actions[action].format(env['USER_ID']))
            sleep(random(args.min, args.max))

    info('Logout')
    d.get(logout)
    el = d.find_element_by_xpath('//*[@id="content"]/div/form/div[2]/button')
    el.click()

    if args.vnc:
        process_vnc.terminate()
        process_vnc.kill()

    process_vfb.terminate()
    process_vfb.kill()
