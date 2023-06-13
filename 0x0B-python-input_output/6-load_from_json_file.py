#!/usr/bin/python3
"""Defining a JSON file reading function"""
import json


def load_from_json_file(filename):
    """creating a python object from a json file"""
    with open(filename) as f:
        return json.load(f)
