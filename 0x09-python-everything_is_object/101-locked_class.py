#!/usr/bin/python3
"""Defining a locked class"""


class LockedClass:
    """
    function prevents user from dynamically creating a new instance attribte
    """

    __slots__ = ["first_name"]
