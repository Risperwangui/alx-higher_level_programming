#!/usr/bin/python3
"""Defining a square-printing function"""


def print_square(size):
    """Prints a swuare with the # character
    Args:
        size (int): the height/width of the square.
    Raises:
        ValueError: if the size is < 0
        TypeError: if the size is not an integer,
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
