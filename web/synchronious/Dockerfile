FROM python:3.7.2-alpine3.8

COPY run.py /opt/

RUN apk add --no-cache curl

ENTRYPOINT ["python3", "-u", "/opt/run.py"]
