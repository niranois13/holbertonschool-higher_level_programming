#!/usr/bin/python3
"""Module compiled with python3"""


class Square:
    """"Class defining a Square, for now printing empty stuff"""
    def __init__(self, size=0):
        self.__size = size
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of Square"""
        return self.__size * self.__size
