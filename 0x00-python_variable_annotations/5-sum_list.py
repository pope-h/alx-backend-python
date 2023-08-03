#!/usr/bin/python3
"""Defines type-annotated function sum_list"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Accepts a list of floats as argument & returns their sum as a float"""
    return sum(input_list)
