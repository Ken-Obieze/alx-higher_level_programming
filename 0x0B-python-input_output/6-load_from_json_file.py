#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”
"""

def load_from_json_file(filename):
    """creates method"""
    with ope(filename) as f:
        return json.load(f)
