#!/usr/bin/env python3
"""Defines a type-annotated function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_function(num: float) -> float:
        return num * multiplier
    return multiplier_function
