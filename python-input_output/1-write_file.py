#!/usr/bin/python3
"""Module compiled with Python3"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF-8)
    and returns the number of characters written"""
    with open(filename, 'w', encoding="utf-8") as f:
        write_data = f.write(text)
        return len(text)
