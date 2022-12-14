#!/usr/bin/python3
""" 5-text_indentation Module"""


def text_indentation(text):
    """
        prints text with 2 new lines after . ? or :
        Args:
            text (str) = text to be formatted
    """

    temp = ""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if len(text) is 0:
        return

    for letter in text:
        temp += letter
        if letter in ["?", ":", "."]:
            while temp[0] is " ":
                temp = temp[1:]
            print(temp)
            print()
            temp = ""
    if len(temp) != 0:
        while temp[0] is " ":
            temp = temp[1:]
        print(temp, end="")
