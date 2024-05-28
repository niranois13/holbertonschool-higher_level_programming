#!/usr/bin/python3
"""Module compiled by Python3"""
import json


def serialize_and_save_to_file(data, filename):
    """Function that serializes and saves data to the specified file"""
    with open(filename, 'w', encoding="UTF-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Function that loads and deserializes data from the specified file"""
    with open(filename, 'r', encoding="UTF-8") as f:
        data = json.load(f)
    return data
