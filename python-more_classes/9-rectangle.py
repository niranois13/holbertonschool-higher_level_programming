#!/usr/bin/python3
"""Module compiled with Python3"""


class Rectangle:
    """definition of the class Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the height and width of the Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return cls(size, size)

    def area(self):
        """Returns the area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest Rectangle (based on area)"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_rect_1 = Rectangle.area(rect_1)
        area_rect_2 = Rectangle.area(rect_2)
        return rect_1 if area_rect_1 >= area_rect_2 else rect_2

    def __str__(self):
        """Returns a list 'rectangle' in order to print Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle = []
        for j in range(self.__height):
            for i in range(self.__width):
                rectangle.append(str(self.print_symbol))
            rectangle.append("\n")
        if rectangle:
            rectangle.pop()
        return ("".join(rectangle))

    def __repr__(self):
        """Returns a string representation of Rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an instance is terminated"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
