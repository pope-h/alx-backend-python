#!/usr/bin/env python3
"""Define a type-annotated function"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Accepts an iterable sequence and returns a list of tuples"""
    return [(i, len(i)) for i in lst]
