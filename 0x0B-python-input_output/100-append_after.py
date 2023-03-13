#!/usr/bin/python3
"""Module for appending after a keyword."""


def append_after(filename="", search_string="", new_string=""):
    """Append str after lines that include a keyword."""

    with open(filename, mode="r+", encoding="utf-8") as f:
        txt = ""
        for line in f:
            txt += line
            if search_string in line:
                txt += new_string
        f.seek(0)
        f.write(txt)
