#!/usr/bin/python3
"""A script that takes in a url,sends a request to the url"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    req = request.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
