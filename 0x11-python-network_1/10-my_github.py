#!/usr/bin/python3
"""Uses GitHub API to display ID.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=basic)
    print(r.json().get("id"))
