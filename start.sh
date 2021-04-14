#!/bin/sh

chmod a+w /dev/pts/0
python3 /home/archiver.py &
sed -i 's/#   dir-listing.activate      = "enable"/dir-listing.activate = "enable"/g' /etc/lighttpd/lighttpd.conf 
exec lighttpd -D -f /etc/lighttpd/lighttpd.conf
