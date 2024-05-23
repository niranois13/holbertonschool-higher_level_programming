#!/usr/bin/python3
"""Module to create a function to print square"""


def print_square(size):
    """
    Method that prints a square
    :param size: int - size (length) of the square to print
    :raises TypeError: if size is not an integer
    :raises TypeError: if size is negative
    :Returns: None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")

    for x in range(size):
        print("#" * size)
