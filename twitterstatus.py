#!bin/python

import json
from twitter import Twitter, OAuth, TwitterHTTPError
from time    import sleep
from sys     import exit

try:
    from config  import *
except Exception as e:
    print("ERROR: Could not import config. Make sure config.py exists.")

try:
    twitter = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
                  CONSUMER_KEY, CONSUMER_SECRET))
except Exception as e:
    print('Error in twitter init: ' + e)
    exit(255)

def write_status(status):
    status_file = open(STATUS_FILE, 'w+')
    status_file.write(json.dumps({'status': status}))

def update(status):
    try:
        status_file = open(STATUS_FILE, 'r')
    except IOError as e:
        print('WARN: problem with status file, writing new one')
        write_status(status.read())
        return

    try:
        last_status = json.loads(status_file.read())
    except Exception as e:
        print('WARN: problem with status file, writing new one')
        write_status(status)
        return

    if status == True and last_status['status'] == False:
        text = 'Space is open!'
    elif status == False and last_status['status'] == True:
        text = 'Space is closed!'
    else:
        return

    try:
        twitter.statuses.update(status=text)
    except TwitterHTTPError as e:
        print('Error while updating status: ' + e)
        return


try:
    twitter.direct_messages.new(user='mkzer0', text='Twitter Bot Startup')
except Exception as e:
    print('Error sending direct message: ' + e)

while 1:
    try:
        status = json.loads(open(CURRENT_STATUS, 'r').read())
        print('status: ' + str(status['state']['open']))
    except FileNotFoundError as e:
        print("Could not find or open status file '" + CURRENT_STATUS + "'")
        exit(255)
    except Exception as e:
        try:
            twitter.direct_messages.new(user='mkzer0', text='Twitter Bot Error')
        except Exception:
            pass
        print('Error loading current status: ' + e)
    else:
        update(status=status['state']['open'])
        write_status(status=status['state']['open'])

    sleep(60)
