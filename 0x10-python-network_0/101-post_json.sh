#!/bin/bash
# this sends a JSON POST request to a given url
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
