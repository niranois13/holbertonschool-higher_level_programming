#!/usr/bin/python3
"""Module compiled with Python3"""


class MyList(list):
    """Definition of a class MyList, that inherits from list"""

    def print_sorted(self):
        """Method that prints the list, sorted in ascending order"""
        print("{}".format(sorted(self)))
