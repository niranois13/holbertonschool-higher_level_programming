#!/usr/bin/python3
"""This module was compiled with Python3"""
import csv
import json


def convert_csv_to_json(csv_file , json_file):
    """Function that converts a csv file to json_file"""
    data = {}

    with open(csv_file, encoding="UTF-8") as csvf:
        csvReader = csv.DictReader(csvf)
        i = 0
        for rows in csvReader:
            key = rows[i]
            data[key] = rows
            i += 1

    with open(json_file, 'w', encoding="UTF-8") as jsonf:
        jsonf.write(json.dump(data))

        

