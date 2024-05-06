import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """
    This asynchronous coroutine spawns n instances of wait_random
    concurrently and returns a list
    of the delays in ascending order without using sort().

    Args:
        n (int): The number of times to wait for a random delay.
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
        list[float]: A list of delays in ascending order.
    """
    delays = []
    tasks = []
    for _ in range(n):
        # Create tasks for each wait_random call
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

      # Append delays to the list while maintaining order
    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays