#!/usr/bin/python3
"""Module compiled with Python3"""
import pickle


class CustomObject:
    """Defines a class CustomObject that serializes and
    deserializes custom Pyhton objects with the pickel module.
    It also displays stuff"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """Method that serializes a custom Python object"""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """Method that deserializes a pickle file"""
        with open(filename, 'rb') as file:
            pickle.load(file)

    def display(self):
        """Method that displays the Python and pickle files"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))
