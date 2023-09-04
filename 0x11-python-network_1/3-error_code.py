#!/usr/bin/python3
"""A scriot that uses urllib to send a request"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
