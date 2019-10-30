#!/usr/bin/env bash

echo $(curl -s -o /dev/null -w "%{http_code}" $1)
