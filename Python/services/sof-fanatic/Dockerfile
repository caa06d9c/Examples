FROM alpine
LABEL maintainer="Dmitrii Demin <mail@demin.co>"

COPY  . /opt/
WORKDIR /opt/

ENV DISPLAY=:0

RUN apk update && \
    apk add --update --no-cache python3 \
                                py3-pip \
                                x11vnc \
                                xvfb \
                                chromium \
                                chromium-chromedriver && \
    pip3 install -r requirements.txt && \
    apk del py3-pip && \
    rm -Rf /var/cache/apk/*

ENTRYPOINT ["/usr/bin/env", "python3", "-u", "/opt/run.py"]
