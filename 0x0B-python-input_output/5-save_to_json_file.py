#!/usr/bin/python3
"""
 function that writes an Object to a text file,
 using a JSON representation
"""

def save_to_json_file(my_obj, filename):
    """
    method/module for writing obj to text
    """
    j = json.dump(my_obj, filename)
    return (j)
