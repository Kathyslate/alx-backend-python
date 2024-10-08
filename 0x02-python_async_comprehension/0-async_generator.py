#!/usr/bin/env python3
'''Task.
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Generates a 10 number sequence.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
