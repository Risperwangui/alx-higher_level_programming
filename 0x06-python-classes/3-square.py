#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """Representing a Square"""

    def __init__(self, size=0):
        """Initilizing a new Square

        Args:
            size (int): This is the size of a new square.
            """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This returns the current area of a square"""
        return (self.__size * self.__size)
