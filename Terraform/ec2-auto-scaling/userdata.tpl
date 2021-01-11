#!/usr/bin/env bash

sudo bash -c "yum -y update && \
              yum -y install docker && \
              service docker start && \
              usermod -a -G docker ec2-user && \
              reboot -y"

docker rm -v -f app || true
docker run -d -p 80:8080 --name app caa06d9c/echo --tag "$(hostname | cut -d '-' -f 4,5)"
