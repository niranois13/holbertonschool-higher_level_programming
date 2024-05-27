#!/usr/bin/python3
"""Module compiled with Python3"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF-8) and
    returns the number of characters added"""
    with open(filename, 'a', encoding="utf-8") as f:
        write_data = f.write(text)
        return len(text)
