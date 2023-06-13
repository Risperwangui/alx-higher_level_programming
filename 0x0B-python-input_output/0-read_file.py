#!/usr/bin/python3
"""Defining a text file-reading function"""


def read_file(filename=""):
    """Printing the contents of a text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
