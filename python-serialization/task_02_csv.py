#!/usr/bin/python3
"""This module was compiled with Python3"""
import csv
import json


def convert_csv_to_json(filename):
    """Function that converts a csv file to json_file"""
    json_file='data.json'
    try:
        with open(filename, 'r', encoding="UTF-8") as csvf:
            csvReader = csv.DictReader(csvf)
            data = list(csvReader)
        with open(json_file, 'w', encoding="UTF-8") as jsonf:
            json.dump(data, jsonf)
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
