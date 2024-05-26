#!/usr/bin/python3
"""Module compiled with Python3"""


from abc import ABC, abstractmethod

class Animal(ABC):
    """Defines the abstract class Animal, using the ABC module"""

    @abstractmethod
    def sound(self):
        """Abstract method that prints the sound of given Animal"""
        pass

class Dog(Animal):
    """Defines the subclass Dog, that inherits from superclass Animal"""

    def sound(self):
        """Method that returns a string of the sound of Dog"""
        return ("Bark")

class Cat(Animal):
    """Defines the subclass Cat, that inherits from superclass Animal"""

    def sound(self):
        """Method that returns a string of the sound of Cat"""
        return ("Meow")
