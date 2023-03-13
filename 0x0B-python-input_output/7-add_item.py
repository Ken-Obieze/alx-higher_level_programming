#!/usr/bin/python3
"""Module implement a scriptthat adds all args to a list."""
import sys
import json


if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file
    load_firom_json_file = __import__("6-load_from_json_file.py").load_from_json_file
    contents = load_from_json_file("add_item.json")
    for i in range(1, len(sys.argv)):
        contents.append(sys.argv[i])
    save_to_json_file(contents, "add_item.json")
