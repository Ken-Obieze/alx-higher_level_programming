#!/usr/bin/python3
""" Module to return the JSON representation of an object (string)."""
import json


def to_json_string(my_obj):
    """
    method for JSON conversion
    """
    j = json.dumps(my_obj)
    return (j)
