[![Docker badge](https://img.shields.io/docker/pulls/caa06d9c/cronjob.svg)](https://hub.docker.com/r/caa06d9c/cronjob/)

# Cronjob
It emulates some activity as a cronjob, can exit with required status code (or random) after some time.
Kubernetes manifest is [here](./manifest.yml)

Simple usage:
```console
# -e - exit code (-1 is default and means random)
# -c - amount of streams (5 is default)
# -t - timeout in seconds (30 is default)

docker run -t --rm caa06d9c/cronjob -e 1 c 20 -t 30
```
