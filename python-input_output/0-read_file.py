#!/usr/bin/python3
"""Module compiled with Python3"""


def read_file(filename=""):
    """function that reads a text file (UTF-8) and prints it to stdout"""
    with open('my_file_0.txt', 'r', encoding="utf-8") as f:
        read_data = f.read()
        print("{}".format(read_data))
