#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from twitter import Twitter, OAuth, TwitterHTTPError
from time import sleep
from sys import exit
from random import choice

try:
    import config
except ImportError as e:
    print("ERROR: Could not import config. Make sure config.py exists.")

try:
    from wordlist import wordlist

    if config.LANGUAGE:
        WORDLIST = wordlist(config.LANGUAGE)
except ImportError:
    WORDLIST = [
        ['The space'],
        ['is'],
        ['open'],
        ['closed'],
        [''],
        ['']
    ]

try:
    twitter = Twitter(auth=OAuth(
                            config.OAUTH_TOKEN,
                            config.OAUTH_SECRET,
                            config.CONSUMER_KEY,
                            config.CONSUMER_SECRET))
except Exception as e:
    print('Error in twitter init: ' + e)
    exit(255)


def write_status(status):
    status_file = open(config.STATUS_FILE, 'w+')
    status_file.write(json.dumps({'status': status}))


def generate_phrase(open_status=True):
    phrase = choice(WORDLIST[0]) + " "
    phrase += choice(WORDLIST[1]) + " "

    if open_status:
        phrase += choice(WORDLIST[2]) + ". "
    else:
        phrase += choice(WORDLIST[3]) + ". "

    if choice([True, False]):
        if open_status:
            phrase += choice(WORDLIST[4]).title() + "!"
        else:
            phrase += choice(WORDLIST[5]).title() + "!"

    return phrase


def update(status):
    try:
        status_file = open(config.STATUS_FILE, 'r')
    except IOError as e:
        print('WARN: problem with status file, writing new one')
        write_status(status)
        return

    try:
        last_status = json.loads(status_file.read())
    except Exception as e:
        print('WARN: problem with status file, writing new one')
        write_status(status)
        return

    if status and not last_status['status']:
        text = generate_phrase(True)
    elif not status and last_status['status']:
        text = generate_phrase(False)
    else:
        return

    try:
        twitter.statuses.update(status=text)
    except TwitterHTTPError as e:
        print('Error while updating status: ' + e)
        return


try:
    twitter.direct_messages.new(
        user=config.ADMIN_NAME,
        text='Twitter Bot Startup'
    )
except Exception as e:
    print('Error sending direct message: ' + str(e))

while 1:
    try:
        status = json.loads(open(config.CURRENT_STATUS, 'r').read())
        print('status: ' + str(status['state']['open']))
    except FileNotFoundError as e:
        print("Could not find or open status file '" +
              config.CURRENT_STATUS + "'")
        exit(255)
    except Exception as e:
        try:
            twitter.direct_messages.new(
                user=config.ADMIN_NAME, text='Twitter Bot Error'
            )
        except Exception:
            pass
        print('Error loading current status: ' + e)
    else:
        update(status=status['state']['open'])
        write_status(status=status['state']['open'])

    sleep(60)
