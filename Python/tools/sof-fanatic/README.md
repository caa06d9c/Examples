[![Docker badge](https://img.shields.io/docker/pulls/caa06d9c/sof-fanatic.svg)](https://hub.docker.com/r/caa06d9c/sof-fanatic/)

# SOF - fanatic
It allows to emulate user activity to collect Enthusiast and Fanatic badges at StackOverflow.

Simple usage:
```console
docker run -t --rm -p 5900:5900 -e USER_ID=${SOF_ID} -e USERNAME=${SOF_USERNAME} -e PASSWORD=${SOF_PASSWORD} -e VNC_P=${VNC_PASSWORD} caa06d9c/sof-fanatic --min 5 --max 10 --actions user reputatuion question --tags linux bash python --vnc --questions 5
```
Connect to container in MacOS:
```
Finder->cmd+k->vnc://localhost:5900
```
