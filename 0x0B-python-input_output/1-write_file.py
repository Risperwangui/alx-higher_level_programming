#!/usr/bin/python3
"""Defining a file-writing function"""


def write_file(filename="", text=""):
    """writing a string to a UTF8 textfile"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
