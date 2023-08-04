#!/usr/bin/env python3
"""Defines a type-annotated function"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """Accepts a Mapping, Any & Typevar and returns TypeVar or Any"""
    if key in dct:
        return dct[key]
    else:
        return default
