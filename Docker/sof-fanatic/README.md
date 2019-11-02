[![Docker badge](https://img.shields.io/docker/pulls/caa06d9c/sof-fanatic.svg)](https://hub.docker.com/r/caa06d9c/sof-fanatic/)

# SOF - fanatic
It allows to emulate user activity to collect Enthusiast and Fanatic badges at StackOverflow.

Simple usage:
```console
docker run -t --rm -p 5900:5900 -e MIN=5 -e MAX=10 -e USER_ID=${SOF_ID} -e USERNAME=${SOF_USERNAME} -e PASSWORD=${SOF_PASSWORD} -e VNC_P=${VNC_PASSWORD} -e TAGS="bash python linux" caa06d9c/sof-fanatic
```
Connect to container in MacOS:
```
Finder->cmd+k->vnc://localhost:5900
```
