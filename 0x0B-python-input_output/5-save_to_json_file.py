#!/usr/bin/python3
"""
    Module to write an Object to a text file using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    method/module for writing obj to text
    """
    with open(filename, "w") as jf:
        json.dump(my_obj, jf)
