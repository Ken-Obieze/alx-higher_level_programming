#!/usr/bin/python3
"""
Module return an object (Python data structure) represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    module for decoding JSON.
    """
    js = json.loads(my_str)
    return (js)
