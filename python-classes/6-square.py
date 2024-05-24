#!/usr/bin/python3
"""Module compiled with python3"""


class Square:
    """"Class defining a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the size of the Square"""
        self.__size = size
        self.position = position

    def area(self):
        """Returns the area of Square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints Square"""
        pos0 = self.__position[0]
        pos1 = self.__position[1]
        x = 0
        if self.__size <= 0:
            print()
        else:
            while pos1 > 0:
                print()
                pos1 -= 1

            for _ in range(self.__size):
                print(" " * pos0 + "#" * self.__size)

    @property
    def size(self):
        """Getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of Square"""
        self.__size = value
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """Getter method for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of Square"""
        self.__position = value
        if isinstance(value, tuple) is not True or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[0], int) is not True or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[1], int) is not True or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
