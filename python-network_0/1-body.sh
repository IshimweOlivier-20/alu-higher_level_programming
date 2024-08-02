#!bin/bash
#sends a request and displays responses
curl -sI "$1" | grep 'Content-Length' | cut -d " " -f2
