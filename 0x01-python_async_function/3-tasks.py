
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int = 10) -> float:
  """
  This function creates and returns an asyncio.Task that waits for a random delay
  between 0 and max_delay (inclusive) seconds.

  Args:
      max_delay (int): The maximum delay in seconds.

  Returns:
      asyncio.Task: A task object that can be used to await the random delay.
  """
    """
    This internal async function waits for the random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

