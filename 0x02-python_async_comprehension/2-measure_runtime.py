#!/usr/bin/env python3
"""Defines measure_runtime"""

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Measures the runtime of parallel coroutines"""
    start = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    stop = asyncio.get_event_loop().time()
    return stop - start
