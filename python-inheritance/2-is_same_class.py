#!/usr/bin/python3
"""Module compiled with Python3"""


def is_same_class(obj, a_class):
    """
    Method to check if object is exactly an instance of the specified class
    :param obj: the object to check
    :param a_class: the class to compare with
    :Returns: True if obj is same class, False otherwise
    """
    return isinstance(obj, a_class)
