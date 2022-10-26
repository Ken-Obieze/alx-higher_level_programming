#!/usr/bin/python3
"""
function that returns the JSON representation 
of an object (string):
"""

def to_json_string(my_obj):
    """
    method for JSON conversion
    """
    j = json.dumps(my_obj)
    return (j)
