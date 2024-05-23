#!/usr/bin/python3
"""Module compiled with Python3"""


def say_my_name(first_name, last_name=""):
    """
    Method the prints given first name and last name.

    :param first_name: str - The first name to print
    :param last_name: str - The last name to print
    :raises Typerror: if first name or last name are not strings
    :Returns: None
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
