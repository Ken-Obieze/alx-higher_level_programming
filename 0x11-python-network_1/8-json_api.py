#!/usr/bin/python3
"""Sends a POST to http://0.0.0.0:5000/search_user with a letter as parameter.

Usage: ./8-json_api.py <letter>
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    dict_load = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=dict_load)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
