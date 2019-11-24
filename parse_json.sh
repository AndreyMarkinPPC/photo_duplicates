#! /bin/bash

title=$(cat $1 | jq -r '.title')
timestamp=$(cat $1 | jq -r '.photoTakenTime.timestamp')
lat=$(cat $1 | jq -r '.geoData.latitude')
lon=$(cat $1 | jq -r '.geoData.longitude')
alt=$(cat $1 | jq -r '.geoData.altitude')

psql -U am -d google_photos \
-c  "insert into photo_info values ('$title', $timestamp, $lat, $lon, $alt);"
