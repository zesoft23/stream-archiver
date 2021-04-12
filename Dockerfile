# Dockerfile for lighttpd

FROM alpine:latest

RUN apk add --no-cache tzdata
ENV TZ=America/New_York

RUN apk add --update --no-cache \
	lighttpd \
	lighttpd-mod_auth \
  && rm -rf /var/cache/apk/*

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

# Just the default lighttpd files...
#COPY etc/lighttpd/* /etc/lighttpd/
COPY start.sh /usr/local/bin/
# Grab the archiver script
COPY archiver.py /home/
COPY streams.json /home/

EXPOSE 80

VOLUME /var/www/localhost
VOLUME /etc/lighttpd

CMD ["start.sh"]
