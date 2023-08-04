#!/usr/bin/env python3
"""Defines a type-annotated function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Accepts a float as argument and returns a function of float"""
    def multiplier_function(num: float) -> float:
        return num * multiplier
    return multiplier_function
