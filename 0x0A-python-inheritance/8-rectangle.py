#!/usr/bin/python3
"""Defining a class Rectangle"""
BaseGeometry = __import__('7-bse_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass of geometry"""

    def __init__(self, width, height):
        """initializing attrributes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
