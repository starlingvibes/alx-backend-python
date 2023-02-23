#!/usr/bin/env python3
"""
Task 0's module
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async_generator coroutine that will loop 10 times
    then wait 1 second each time and yield a random number between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
