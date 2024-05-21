#!/usr/bin/python3
"""Module compiled with Python3"""


def add_integer(a, b=98):
    """Method that adds two integers
    Floats are accepted but casted into integers
    Other types raise TypeError"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
