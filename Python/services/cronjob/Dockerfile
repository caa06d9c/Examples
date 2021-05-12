FROM python:3.8-alpine
LABEL maintainer="Dmitrii Demin <mail@demin.co>"

WORKDIR /opt/
COPY . /opt/

RUN apk update && \
    pip install -r requirements.txt && \
    rm -Rf /var/cache/apk/*

USER nobody

ENTRYPOINT ["/usr/bin/env", "python3", "-u", "/opt/run.py"]
