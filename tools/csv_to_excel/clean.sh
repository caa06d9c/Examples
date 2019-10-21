#!/usr/bin/env bash

#!/usr/bin/env bash

if [[ "$(pwd | rev | cut -d '/' -f 1)" == "$(echo 'csv_to_excel' | rev)" ]]; then
   rm -f *.xlsx
else
    echo "check the working directory"
    exit 1
fi

