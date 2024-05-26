#!/usr/bin/python3
"""Module compiled with Python3"""

from typing import SupportsIndex


class VerboseList(list):
    """Defines a class VerboseList that enhances the built-in method list.
    It prints a message when append(), extend(), remove() or pop() are used."""

    def append(self, object):
        """
        Method that prints a message explicitly naming what is added to a list
        when .append() is used.
        :param object: item to be added to the list
        """
        print("Added [{}] to the list".format(object))
        return super().append(object)

    def extend(self, iterable):
        """
        Method that prints a message explicitly naming what is added to a list
        when .extend() is used.
        :param iterable: an iterable item containing elements to add to the list
        """
        to_add = len(iterable)
        print("Extended the list with [{}] items.".format(to_add))
        return super().extend(iterable)

    def remove(self, value):
        """
        Method that removes the first occurrence of value from
        list and print a notification.
        :param value: Value to be removed from the list.
        """
        print("Removed [{}] from the list.".format(value))
        return super().remove(value)

    def pop(self, index=-1):
        """
        Method that removes an item at index (by default, last item of list).
        Prints a notification at removal of the item.
        :param index: Position of the item to remove. Default is last item.
        """
        item = self[index]
        print("Popped [{}] from the list".format(item))
        return super().pop(index)
