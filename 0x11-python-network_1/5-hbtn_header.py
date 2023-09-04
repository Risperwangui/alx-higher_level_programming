#!/usr/bin/python3
"""Displaying the x-request-id header variable"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    re = requests.get(url)
    print(re.headers.get("X-Request-Id"))
