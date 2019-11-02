[![Docker badge](https://img.shields.io/docker/pulls/caa06d9c/support.svg)](https://hub.docker.com/r/caa06d9c/support/)

# Support
Alpine-based Docker image for testing and debug purposes. 

The image tagged *latest* has:
+ mysql-client
+ postgresql-client
+ curl
+ git
+ nc
+ dig

The image tagged *mongo* has:
+ mongo

Simple usage:
```console
docker exec -it --rm caa06d9c/support sh
```
Simple curl usage:
```console
docker run -t --rm caa06d9c/support curl google.com
```
Advanced curl usage (post json as payload):
```console
body=$(cat<<EOF
{"SomeKey": [{"SomeItem": "SomeValue"}]}
EOF)

docker run -t --rm caa06d9c/support curl -XPOST --header 'Content-Type: application/json' -d "${body}" ${URL}
```
Works as service:
```console
docker run -d caa06d9c/support
```
Send a mongo command (drop database):
```console
docker run -t --rm caa06d9c/support:mongo sh -c "echo 'db.dropDatabase();' | mongo --host ${host} ${database}"
```
