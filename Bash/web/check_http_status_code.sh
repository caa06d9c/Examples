#!/usr/bin/env bash

if [[ "${1}" == '' ]]; then echo "URL is empty "; exit 1; fi

curl -s -o /dev/null -w "%{http_code}" "${1}"
