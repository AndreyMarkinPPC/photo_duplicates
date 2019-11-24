#! /bin/bash

find $1  -name "*jpg.json" -exec ./parse_json.sh '{}' \;
