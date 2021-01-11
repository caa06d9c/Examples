FROM alpine:3.6

LABEL maintainer="Dmitrii Demin <mail@demin.co>"

RUN apk update \
&&  apk add --update --no-cache mongodb \
&&  rm -Rf /var/cache/apk/* \
&&  echo $'#!/bin/sh\n\
while true; do sleep 60; done\n'\
>> /usr/local/bin/run \
&& chmod +x /usr/local/bin/run

CMD ["/usr/local/bin/run"]
