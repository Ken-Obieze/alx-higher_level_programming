#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status.

Usage: ./4-hbtn_status.py | cat -e
""" 
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    r = requests.get(url)
    print("Body response:\n\t- type: {}\n\t- content: {}"
            .format(type(r.text), r.text))
