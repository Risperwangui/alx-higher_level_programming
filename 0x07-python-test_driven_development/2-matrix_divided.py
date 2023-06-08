#!/usr/bin/pyth0n3
"""Defining a division function"""


def matrix_divided(matrix, div):
    """Dividing all elemnts of a matrix.
    Args:
        div (int/float): This is the divisor
        matrix (list): a list of ints and floats.
    Raises:
        TypeError: if the matrix contains non-numbers
        TypeError: if the div is not an integer or float
        ZeroDivisionError: if the div is 0
    Returns:
        A matrix with the division
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of ""integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
