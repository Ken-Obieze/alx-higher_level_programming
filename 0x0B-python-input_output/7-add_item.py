#!/usr/bin/python3
"""
Module implement a scriptthat adds all args to a list.
"""
import sys
save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file
load_firom_json_file = __import__("6-load_from_json_file.py").load_from_json_file:

if __name__ == "__main__":
    contents = load_from_json_file("add_item.json")
    contents.extend(sys.argv[1:])
    save_to_json_file(contnts, "add_item.json")
