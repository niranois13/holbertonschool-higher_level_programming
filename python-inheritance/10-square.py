#!/usr/bin/python3
"""Module compiled with Python3"""


class BaseGeometry:
    """Defines the class BaseGeometry"""

    def area(self):
        """Method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates a value type"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Defines the class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes Rectangle with a width and a height,
        validated by interger_validator"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string that is a Rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


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
