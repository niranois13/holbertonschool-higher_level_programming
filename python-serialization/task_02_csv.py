#!/usr/bin/python3
"""This module was compiled with Python3"""
import csv
import json


def convert_csv_to_json(csv_file, json_file):
    """Function that converts a csv file to json_file"""
    with open(csv_file, encoding="UTF-8") as csvf:
        csvReader = csv.DictReader(csvf)
        data = [row for row in csvReader]
    with open(json_file, 'w', encoding="UTF-8") as jsonf:
        json.dump(data, jsonf)
