#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -sG "$1" -H "X-School-User-Id: 98"
