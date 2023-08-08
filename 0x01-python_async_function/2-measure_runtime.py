#!/usr/bin/env python3
"""Defines measure_time function"""

import time
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay)"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop_time = time.time()

    total_time = stop_time - start_time
    avg_time = total_time / n
    return avg_time
