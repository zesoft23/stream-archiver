#!/bin/python3

"""
Archives files in the provided streams file
into chunks.

jack@jackmcintoshthomson.com

"""

import urllib.request
import time
import json

with open("streams.json") as jo:
    json_url = json.load(jo)
url = json_url["main"]
filedata = urllib.request.urlopen(url)
# This Chunk value is naive... what should it be?
CHUNK = 16 * 1024
duration = 60 * 30
print(f"Grabbing {url}")
numb = 0
now = time.time()
# two hours test time
while time.time - now < 120 * 60:
    numb = numb + 1
    with open(f"foo_{numb}.mp3", 'wb') as f:
        now = time.time()
        while time.time() - now < json_url['time_chunks']:
            f.write(filedata.read(CHUNK))
