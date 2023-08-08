#!/usr/bin/env python3
"""Defines async_generator"""

import asyncio
import random


async def async_generator():
    """Yields a random int 10 times"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
