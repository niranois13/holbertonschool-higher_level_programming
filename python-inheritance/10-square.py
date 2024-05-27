#!/usr/bin/python3
"""Module compiled with Python3"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines the class Square that inherites from Rectangle"""

    def __init__(self, size):
        """Initializes Square with a size attribute,
        validated by interger_validator"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Method that returns the area of Square"""
        return self.__size * self.__size
