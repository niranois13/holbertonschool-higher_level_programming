#!/usr/bin/python3
"""Module compiled with Python3"""


def class_to_json(obj):
    """function that returns a dictionary description with simple data
    structure for JSON serialization of an object"""
    return obj.__dict__


