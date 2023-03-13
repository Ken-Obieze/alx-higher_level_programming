#!/usr/bin/python3
"""Module to return dict description with simple data structure"""
import json


def class_to_json(obj):
    """retun dict representation with simple data"""
    return obj.__dict__
