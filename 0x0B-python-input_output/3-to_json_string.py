#!/usr/bin/python3
"""Defining a string-function to JSON function"""
import json


def to_json_string(my_obj):
    """Returning the JSON representation"""
    return json.dumps(my_obj)
