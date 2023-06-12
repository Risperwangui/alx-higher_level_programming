#!/usr/bin/python3
"""Defining a class MyInt"""


class MyInt(int):
    """inverting int operators"""

    def __eq__(self, value):
        """overriding the equal operator with !."""
        return self.real != value

    def __ne__(self, value):
        """overriding operators"""
        return self.real == value
