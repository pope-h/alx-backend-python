#!/usr/bin/env python3
"""Defines wait_n"""

import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with max_delay"""
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
