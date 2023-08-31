#!/bin/bash
# this sends a get request to a given url
curl -s -o /dev/null -w "%{http_code}" "$1"
