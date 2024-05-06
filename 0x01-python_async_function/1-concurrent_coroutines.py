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

    # Wait for all tasks to complete concurrently
    await asyncio.gather(*tasks)

    # Append delays to the list while maintaining order
    for task in tasks:
        delay = task.result()
        # Use insertion sort to maintain order during appending
        inserted = False
        for i in range(len(delays)):
            if delay <= delays[i]:
                delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            delays.append(delay)

    return delays

# Example usage


async def main():
    # Wait for 3 random delays between 0 and 5 seconds
    delays = await wait_n(3, 5)
    print(f"Delays: {delays}")

if __name__ == "__main__":
    asyncio.run(main())
