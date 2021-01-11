#!/usr/bin/env bash
# 1 - region, 2 - registry
st=1

if [[ "${1}" == '' ]]; then echo "Region is empty "; st=0; fi
if [[ "${2}" == '' ]]; then echo "Registry is empty "; st=0; fi
if [[ st -eq 0 ]]; then exit 1; fi

pass=$(aws ecr get-authorization-token --region "${1}" --output text --query authorizationData[0].authorizationToken | base64 -D | cut -d: -f2)

echo "${pass}" | docker login -u AWS --password-stdin "https://${2}.dkr.ecr.${1}.amazonaws.com"
