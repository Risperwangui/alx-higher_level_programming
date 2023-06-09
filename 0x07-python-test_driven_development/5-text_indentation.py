#!/usr/bin/python3
"""Module to print a text with 2 new line after . ? and : """


def text_indentation(text):
    """prints a text
    Args:
        text (string) : The text.
    Raises:
        TypeError: if the text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
                [line.strip(" ") for line in text.split(delim)])

    print(f"{text}", end="")
