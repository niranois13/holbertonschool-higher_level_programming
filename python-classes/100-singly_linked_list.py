#!/usr/bin/python3
"""Compiled with Python3"""


class Node:
    """Class defining a Node for a single linked list"""

    def __init__(self, data, next_node=None):
        """Initializes the Node with a data and a potential next node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter method for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data for the sigle linked list, must be an int"""
        self.__data = value
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Getter method for the next node"""
        return self.__nextnode

    @next_node.setter
    def next_node(self, value):
        """Sets the next node of the signle linked list"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Class defining SinglyLinkedList"""

    def __init__(self):
        """Initializes SinglyLinkedList with a header node"""
        self.__head = None

    def sorted_insert(self, value):

