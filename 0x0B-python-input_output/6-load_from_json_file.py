#!/usr/bin/python3
"""
    Modulr to  create an Object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """creates method"""
    with open(filename) as jf:
        return json.load(jf)
