#!/usr/bin/python3
"""Module compiled with Python3"""


class Rectangle:
    """definition of the class Rectangle"""

    def __init__(self, height=0, width=0):
        """Initializes the height and width of the Rectangle"""
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
