#!/usr/bin/python3
"""Module compiled with Python3"""


class BaseGeometry:
    """Defines the class BaseGeometry"""

    def integer_validator(self, name, value):
        """Method that validates a value type"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
