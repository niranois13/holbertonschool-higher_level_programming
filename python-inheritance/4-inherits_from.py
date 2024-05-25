#!/usr/bin/python3
"""Module compiled with Python3"""


def inherits_from(obj, a_class):
    """
    Method that checks if object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    :param obj: the object to check.
    :param a_class: the class to compare with.

    :Returns: True if obj is inherited from a_class, False otherwise.
    """
    return type(obj) is not a_class and isinstance(obj, a_class)
