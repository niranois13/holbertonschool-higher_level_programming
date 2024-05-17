#!/usr/bin/python3
"""Module compiled with python3"""


class Square:
    """"Class defining a Square, for now printing empty stuff"""

    def __init__(self, size=0):
        """Initializes the size of the Square"""
        self.__size = size

    def area(self):
        """Returns the area of Square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints Square"""
        x = 0
        if self.__size <= 0:
            print()
        else:
            while x < self.__size:
                y = 0
                while y < self.__size:
                    print("#", end="")
                    y += 1
                print()
                x += 1

    @property
    def size(self):
        """The Getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of Square"""
        self.__size = value
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
