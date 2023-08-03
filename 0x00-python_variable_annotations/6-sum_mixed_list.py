#!/usr/bin/python3
"""Defines a type-annotated function"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Accepts a list of integers and floats & returns their sum as a float"""
    return sum(mxd_lst)
