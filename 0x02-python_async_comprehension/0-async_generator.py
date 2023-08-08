#!/usr/bin/env python3
"""Defines async_generator"""

import asyncio
from random import random


async def async_generator():
    """Yields a random int 10 times"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random() * 10
