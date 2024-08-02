#!/bin/bash

# This script takes a URL as an argument, sends a request, and displays the size of the response body in bytes

if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL="$1"

curl -s -o /dev/null -w "%{size_download}\n" "$URL"
