#!/bin/python3

"""
Archives files in the provided streams file
into chunks.

jack@jackmcintoshthomson.com

"""

import urllib.request
import time
import json
import argparse
import datetime
import threading

save_directory = '/var/www/localhost/htdocs/'
json_directory = '/home/streams.json'

def wait_until_half():
    # Ultra naive... to get the correct time + day
    while time.strftime('%M') != '00' or time.strftime('%M') != '30':
        time.sleep(5)

# Load JSON File
with open(json_directory) as jo:
    json_url = json.load(jo)
url = json_url["stream_url"]
# Create stream request object
filedata = urllib.request.urlopen(url)
duration = 30 * 60 # 30 minutes
# This Chunk value is naive... what should it be?
CHUNK = 16 * 1024

while True:
    #thread = threading.Thread(target=wait_until_half)
    #thread.start()
    #thread.join()
    with open(f"{save_directory}/{time.strftime('%a_%H%M')}.mp3", 'wb') as f:
        now = time.time()
        while time.time() - now < duration:
            f.write(filedata.read(CHUNK))

