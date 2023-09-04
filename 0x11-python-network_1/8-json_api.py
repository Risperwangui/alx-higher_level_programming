#!/usr/bin/python3
"""writing a script that takes in a letter and sends a post request"""

import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"

    data = {'q': letter}

    response = requests.port(url, data=data)

    try:
        parsed_response = response.json()

        if parsed_response == {}:
            print("No result")
        else:
            print("[{}] {}".format(parsed_response.get(
                "id"), parsed_response.get("name")))
    except ValueError:
        print("Not a valid JSON")
