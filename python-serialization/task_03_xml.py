#!/usr/bin/python3
"""Module compiled with Python3"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into XML and saves it to a given filename.
    :param dictionary: a python dictionary to serialize
    :param filename: the file in which the serialized dictionary will be saved
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        tree = ET.SubElement(root, key)
        tree.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    Deserializes a XML file into a python dictionary
    :param filename: the file containing the XML data
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for element in root:
        tag = element.tag
        text = element.text
        dictionary[tag] = text
    return dictionary



