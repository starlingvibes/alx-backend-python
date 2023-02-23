#!/usr/bin/env python3

import random
import asyncio

"""
Task 0's module
"""


async def async_generator():
    """async_generator function"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
