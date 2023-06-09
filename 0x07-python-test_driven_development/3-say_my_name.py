#!/usr/bin/python3
"""Defining a name-printing funcction"""


def say_my_name(first_name, last_name=""):
    """Printing a name.
    Args:
        first_name (str): the first name
        second_name (str): the second name
    Raises:
        TypeError:when either the first or the last name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
