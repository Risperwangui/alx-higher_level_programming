#!/usr/bin/python3
"""listing the last 10 recent commits on a given github"""
import sys
import requests


if __name__ == "__main__":
    rep_name = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner, rep_name)

    params = {'per_page': 10}

    response = requests.get(url, params=params)

    commits = response.json()
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
