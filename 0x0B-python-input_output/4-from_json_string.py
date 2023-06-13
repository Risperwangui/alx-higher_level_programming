#!/usr/bin/python3
"""Defining a JSON to object function"""
import json


def from_json_string(my_str):
    """Retturning the Python object"""
    return json.loads(my_str)
