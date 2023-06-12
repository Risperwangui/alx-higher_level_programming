#!/usr/bin/python3
"""Defining a function that adds attributes"""


def add_attribute(obj, att, value):
    """Adding new attributes
    Args:
        att (str): the name of the attribute
        value (any): the value of the attribute
        obj (any): the object
    Raise:
        TypeError: if the att cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise Typeerror("can't add new attribte")
    setattr(obj, att, value)
