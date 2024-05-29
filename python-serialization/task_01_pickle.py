#!/usr/bin/python3
"""Module compiled with Python3"""
import pickle


class CustomObject:
    """Defines a class CustomObject that serializes and
    deserializes custom Python objects with the pickle module.
    It also displays stuff"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Method that displays the CustomObject data"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Method that serializes a custom Python object"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            raise Exception(e)

    @classmethod
    def deserialize(cls, filename):
        """Method that deserializes a pickle file"""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            raise Exception(e)
