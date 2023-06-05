#!/usr/bin/python3
"""Deefining integer addition"""


def add_integer(a, b=98):
    """Returning the addition of a and b

    Float arguments are typecasted into ints

    Raises:
        TypeError: If either a or b is a non-float or non-integer.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
