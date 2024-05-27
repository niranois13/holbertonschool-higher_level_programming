#!/usr/bin/python3
"""Module compiled with Python3"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines the class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes Rectangle with a width and a height,
        validated by interger_validator"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
