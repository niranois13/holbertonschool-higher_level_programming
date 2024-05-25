#!/usr/bin/python3
"""Module compiled with Python3"""


def is_kind_of_class(obj, a_class):
    """
    Method to check if object if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class.

    :param obj: the object to check.
    :param a_class: the class to compare with.

    :Returns: True if obj is same class, False otherwise.
    """
    return isinstance(obj, a_class)
