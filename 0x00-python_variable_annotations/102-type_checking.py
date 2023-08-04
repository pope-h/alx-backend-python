#!/usr/bin/env python3
"""Using mypy to validate piece of code & apply changes"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Make sure to use a tuple instead of a list

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Use an integer for the factor, not a float
