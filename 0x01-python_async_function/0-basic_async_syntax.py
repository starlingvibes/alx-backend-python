#!/usr/bin/env python3

import random
import asyncio

"""
Module to practice the basics of async io
"""


async def wait_random(max_delay: int = 10) -> float:
    """An asynchronous coroutines that takes in an integer argument
    and waits for a random delay
    """
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
