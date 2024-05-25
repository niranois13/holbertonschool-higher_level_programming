#!/usr/bin/python3
"""Module compiled with Python3"""


def lookup(obj):
    """
    Method that returns a list of available attributes and methods of an object
    :param obj: object that has available atributes and methods
    :Returns: a list"""
    return dir(obj)
