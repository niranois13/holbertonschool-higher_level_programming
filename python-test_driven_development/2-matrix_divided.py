#!/usr/bin/python3
"""Module compiled with Python3"""


def matrix_divided(matrix, div):
    """
    Method that divides all elements of a matrix by a divisor

    :param matrix: list of lists (matrix) of int or float - matrix to divide
    :param div: int or float - the divisor

    :raises TypeError: if the matrix contains anything other than int or float
    :raises TypeError: if rows of the matrix are not the same size
    :raises TypeError: if div is not an int or float
    :raises ZeroDivisionError: if div is 0

    :returns: new list of list (matrix) of int or float -
    containing the quotient of each division, rounded to 2 decimal places
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) \
                        of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) \
                        of integers/floats")

    if len({len(row) for row in matrix}) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for j in row:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) \
                                of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = [[round(j / div, 2) for j in row] for row in matrix]
    return new_list
