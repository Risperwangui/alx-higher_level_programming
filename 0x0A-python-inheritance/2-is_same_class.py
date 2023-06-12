#!/usr/bin/python3
"""Defining a class-checking function"""


def is_same_class(obj, a_class):
    """Checking if an object is exactly an instance of a given class.
    Args:
        obj (any): the object
        a_class (type): the class
    Returns:
        if the object is exactly an instance, true
    """
    if type(obj) == a_class:
        return True
    return False
