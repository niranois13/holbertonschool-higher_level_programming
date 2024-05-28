#!/usr/bin/python3
"""Module compiled with Python3"""


class Student:
    """Defines a class Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the class Student with first name, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that retrieves a dict representation of a Student instance"""
        if attrs is None:
            return self.__dict__

        if not isinstance(attrs, list):
            return {}

        json_dict = {}
        for item in attrs:
            if not isinstance(item, str):
                return {}
            if hasattr(self, item):
                json_dict[item] = getattr(self, item)
        return json_dict
