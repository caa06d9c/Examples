#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from time import sleep
from random import randint as random
from os import environ as env
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from subprocess import Popen, PIPE


if __name__ == '__main__':
    url_login = 'https://stackoverflow.com/users/login'
    url_logout = 'https://stackoverflow.com/users/logout'
    url_user = 'https://stackoverflow.com/users/{}'
    url_reputation = url_user + '?tab=reputation'
    url_questions = 'https://stackoverflow.com/questions/tagged/{}'
    url_bounty = url_questions + '?tab=Bounties'

    tags = [i for i in env.get("TAGS").split(" ")]

    sleep_min = int(env['MIN'])
    sleep_max = int(env['MAX'])

    cmd_vfb = ['Xvfb', ':0', '-shmem', '-screen', '0', '1024x768x24', '-fbdir', '/var/tmp']
    cmd_vnc = ['x11vnc', '-display', ':0', '-noxrecord', '-noxfixes', '-noxdamage', '-forever', '-passwd', env['VNC_P']]

    print('Starting')
    process_vfb = Popen(cmd_vfb, stdout=PIPE, stderr=PIPE)
    sleep(5)
    process_vnc = Popen(cmd_vnc, stdout=PIPE, stderr=PIPE)
    sleep(5)

    co = Options()
    co.add_argument("--no-sandbox")
    co.add_argument("--user-data-dir=/root/.chromium/")
    d = webdriver.Chrome(chrome_options=co)

    print('Started')
    d.get(url_login.format(env['USER_ID']))

    print('Login')
    el = d.find_element_by_xpath('//*[@id="email"]')
    el.send_keys(env['USERNAME'])

    el = d.find_element_by_xpath('//*[@id="password"]')
    el.send_keys(env['PASSWORD'])

    el = d.find_element_by_xpath('//*[@id="submit-button"]')
    el.click()

    sleep(random(sleep_min, sleep_max))

    for tag in tags:
        print(tag)
        d.get(url_questions.format(tag))
        sleep(random(sleep_min, sleep_max))

        d.get(url_bounty.format(tag))
        sleep(random(sleep_min, sleep_max))

    print('User')
    d.get(url_user.format(env['USER_ID']))
    sleep(random(sleep_min, sleep_max))

    print('Reputation')
    d.get(url_reputation.format(env['USER_ID']))
    sleep(random(sleep_min, sleep_max))

    print('Logout')
    d.get(url_logout)
    el = d.find_element_by_xpath('//*[@id="content"]/div/form/div[2]/button')
    el.click()

    process_vnc.terminate()
    process_vnc.kill()

    process_vfb.terminate()
    process_vfb.kill()
