[![Docker badge](https://img.shields.io/docker/pulls/caa06d9c/sof-fanatic.svg)](https://hub.docker.com/r/caa06d9c/sof-fanatic/)

# SOF - fanatic
It emulates user activity to collect Enthusiast and Fanatic badges at StackOverflow.

Simple usage:
```console
docker run -t --rm -p 5900:5900 -e USER_ID=${SOF_ID} -e USERNAME=${SOF_USERNAME} -e PASSWORD=${SOF_PASSWORD} -e VNC_P=${VNC_PASSWORD} caa06d9c/sof-fanatic --min 5 --max 10 --actions user reputation question --tags linux bash python --questions 5 --vnc 
```
Connect to container in macOS:
```
Finder->cmd+k->vnc://localhost:5900
```
