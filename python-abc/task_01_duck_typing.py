#!/usr/bin/python3
"""Module compiled with Python3"""


from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Defines the abstract class Shape, using the ABC module"""

    @abstractmethod
    def area(self):
        """Abstract method that calculates the area of Shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method that calculates the perimeter of Shape"""
        pass


class Circle(Shape):
    """Defines the subclass Circle that inherits from abstract class Shape"""

    def __init__(self, radius):
        """
        Initializes the subclass Circle with a radius
        :param radius: int or float - the radius of Cercle"""
        super().__init__()
        self.radius = radius

    def area(self):
        """Method that calculates the area of Circle"""
        return abs(math.pi * (self.radius ** 2))

    def perimeter(self):
        """Method that calculates the perimeter of Cercle"""
        return abs(math.pi * self.radius * 2)


class Rectangle(Shape):
    """Defines the subclass Rectangle that inherits from superclass Shape"""

    def __init__(self, width, height):
        """
        Initializes Rectangle with a width and a height
        :param width: int or float - the width of Rectangle
        :param hight: int or float - the hight of Rectangle
        """
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        """Method that returns the area of Rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """Method that returns the perimeter of Rectangle"""
        return (self.width * 2 + self.height * 2)


def shape_info(Shape):
    """
    Method that prints the area and perimeter of Shape
    :param Shape: An instance of a subclass of Shape
    """
    print("Area: {} ".format(Shape.area()))
    print("Perimeter: {}".format(Shape.perimeter()))
