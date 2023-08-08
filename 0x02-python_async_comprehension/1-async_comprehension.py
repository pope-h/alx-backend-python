#!/usr/bin/env python3
"""Defines async_comprehension"""

import asyncio
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Creates a list of 10 floats from async_generator"""
    random_numbers = [number async for number in async_generator()]
    return random_numbers
