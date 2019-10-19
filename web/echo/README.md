[![Docker badge](https://img.shields.io/docker/pulls/caa06d9c/echo.svg)](https://hub.docker.com/r/caa06d9c/echo/)

# Simple echo server

## Overview

It provides a JSON reply, supports X-Forwarded-* headers (X-Real-IP too). Can work behind a NGINX reverse proxy, see an example in the 
[repository](https://github.com/caa06d9c/python-examples/tree/master/web/echo).

Supported methods:
  - get
  - put
  - post
  - patch
  - delete
  
Supported headers:
  - X-Real-IP ($remote_addr)
  - X-Forwarded-For ($remote_addr)
  - X-Forwarded-Host ($host)
  - Host ($host)
  - X-Forwarded-Port ($server_port)
  - X-Forwarded-Proto ($scheme)
  - X-Forwarded-Request ($request)
  - X-Forwarded-Agent ($http_user_agent)
  
## How to use

```bash
docker run -d -p 8080:8080 caa06d9c/echo
curl localhost:8080/123/123
curl localhost:8080/echo1/123
curl --header 'X-Real-IP: 1.1.1.1' localhost:8080/123/123
```

```bash
# see the docker-compose.yml file in the repository
docker-compose up -d
```
