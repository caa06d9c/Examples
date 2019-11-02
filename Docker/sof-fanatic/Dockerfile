FROM alpine
LABEL maintainer="Dmitrii Demin <mail@demin.co>"

COPY  . /opt/

ENV DISPLAY=:0

RUN apk update && \
    apk add --update --no-cache python \
                                py-pip \
                                x11vnc \
                                xvfb \
                                chromium \
                                chromium-chromedriver && \
    pip install selenium && \
    apk del py-pip && \
    rm -Rf /var/cache/apk/*

ENTRYPOINT ["/usr/bin/env", "python2", "-u", "/opt/run.py"]
