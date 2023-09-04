#!/usr/bin/python3
"""writing a python script that takes your Github credentials"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    re = requests.get("https://api.github.com/user", auth=auth)
    print(re.json().get("id"))
