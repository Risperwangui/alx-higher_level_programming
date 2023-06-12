#!/usr/bin/python3
"""Defining a function that adds attributes"""


def add_attribute(obj, att, value):
    """Adding new attributes
    Args:
        att (str): the name of the attribute
        value (any): the value of the attribute
        obj (any): the object
    Raises:
        TypeError: if the att cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
