#!/usr/bin/env python3
"""Defines a type-annotated function"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Accepts a string & an int OR float v as arguments and returns a tuple"""
    return (k, float(v) ** 2)
