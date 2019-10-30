#!/usr/bin/env bash

region=$1
registry=$2

pass=$(aws ecr get-authorization-token --region ${region} --output text --query authorizationData[0].authorizationToken | base64 -D | cut -d: -f2)

echo ${pass} | docker login -u AWS --password-stdin https://${registry}.dkr.ecr.${region}.amazonaws.com
