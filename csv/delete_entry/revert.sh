#!/usr/bin/env bash

if [[ "$(pwd | rev | cut -d '/' -f 1)" == "$(echo 'delete_entry' | rev)" ]]; then
   rm -f file.csv
   cp file-orig.csv file.csv
else
    echo "check the working directory"
    exit 1
fi
