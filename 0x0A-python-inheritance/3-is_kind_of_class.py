#!/usr/bin/python3
"""Defining an inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """checking if an object is an instance of a class.
    Args
        obj (any) : the object
        a_class (type): the class
    Return: if an object is an instance of a class, true
    """
    if isinstance(obj, a_class):
        return True
    return False
