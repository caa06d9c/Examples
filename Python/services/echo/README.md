[![Docker badge](https://img.shields.io/docker/pulls/caa06d9c/echo.svg)](https://hub.docker.com/r/caa06d9c/echo/)

# Simple echo server

## Overview

It provides a JSON reply, supports X-Forwarded-* headers . Can work behind a Nginx reverse proxy, see an example in the 
[repository](https://github.com/caa06d9c/python-examples/tree/master/web/echo).

Supported methods:
  - get
  - put
  - post
  - patch
  - delete
  
Supported headers:
  - Host ($host)
  - X-Forwarded-Host ($host)
  - X-Forwarded-For ($http_x_forwarded_for)
  - X-Forwarded-Port ($server_port)
  - X-Forwarded-Proto ($scheme)
  - X-Forwarded-Request ($request)
  - X-Forwarded-Agent ($http_user_agent)
  - X-Amzn-Trace-Id
  
## How to use

```bash
docker run -d -p 80:8080 caa06d9c/echo
curl localhost/123/123
curl localhost/echo1/123
```

```bash
# see the docker-compose.yml file in the reverse-proxy repository
# be aware, this example works only on Linux
docker-compose up -d
```
