[![Docker badge](https://img.shields.io/docker/pulls/caa06d9c/cronjob.svg)](https://hub.docker.com/r/caa06d9c/cronjob/)

# Cronjob
It emulates some activity as a cronjob, can exit with required status code (or random) after some time.
Kubernetes manifest is [here](./manifest.yml)

# Parameters
    -e - exit code (0-255), -1 by default, means random
    -c - amount of parallel executions, 5 by default
    -t - execution time in seconds, 30 by default
    -s - amount lines of ouput to ignore, by defaule each 300000 is printed (in each parallel execution)
    
Simple usage:
```console
docker run -t --rm caa06d9c/cronjob -e 0 -c 20 -t 30
```
