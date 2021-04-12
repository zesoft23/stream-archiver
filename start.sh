#!/bin/sh

chmod a+w /dev/pts/0
python3 /home/archiver.py &
exec lighttpd -D -f /etc/lighttpd/lighttpd.conf