#!/usr/bin/python3
"""Module compiled with Pyhton3"""
import json


def from_json_string(my_str):
    """function that returns an object (Python data structure)
    represented by a JSON string"""
    return json.dumps(my_str)
