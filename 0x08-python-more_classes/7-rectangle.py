#!/usr/bin/python3
"""Defining a rectangle"""


class Rectangle:
    """Representing a rectangle.

    Attributes:
        number_of_instances (int) : this is the number of rectangle instances.
        print_symbol (any): representing a string
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing a new rectangle.

        Args:
            height (int): the height of the new rectangle
            width (int): the widthe of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.height = height
        self.width = width

    @property
    def height(self):
        """setting the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """setting the new width of the retangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Returning the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returning the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """returning the printable representation of the rectangle.
        This represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rec = []
        for i in range(self.__height):
            [rec.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        """returning the string representation of the rectangle"""
        rec = "Rectangle(" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return (rec)

    def __del__(self):
        """printing a message for deleting a rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
