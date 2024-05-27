#!/usr/bin/python3
"""Module compiled with Python3"""


class CountedIterator(iter):
    """Defines a class CountedIterator that inherits from the built-in iter()
    It should keep track of the number of items that have been iterated over"""

    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self._iterator)
            self.count += 1
            return item
        except StopIteration:
            raise

