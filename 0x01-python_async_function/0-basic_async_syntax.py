import asyncio
import random


async def wait_random(max_delay=10):
    """
    This asynchronous coroutine waits for a random delay between 0 and max_delay (inclusive) seconds
    and returns the delay value.

    Args:
        max_delay (int, optional): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The random delay between 0 and max_delay (inclusive) seconds.
    """
    delay = random.uniform(
        0, max_delay)  # Generate random delay between 0 and max_delay
    await asyncio.sleep(delay)  # Wait for the random delay asynchronously
    return delay


async def main():
    # Wait for a random delay between 0 and 5 seconds
    delay = await wait_random(5)
    print(f"Waited for {delay:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
