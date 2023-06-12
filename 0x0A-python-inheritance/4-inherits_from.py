#!/usr/bin/python3
"""Defining an inherited class-checking function"""


def inherits_from(obj, a_class):
    """function that returns true if the object is an instance of a class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
