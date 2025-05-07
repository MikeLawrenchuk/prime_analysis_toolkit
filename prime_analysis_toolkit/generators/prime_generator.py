from typing import List
import logging

from prime_analysis_toolkit.constants import MAX_PRIME_LIMIT

logger = logging.getLogger(__name__)

def generate_primes(limit: int) -> List[int]:
    """
    Generate all prime numbers up to a given limit using the Sieve of Eratosthenes.

    Args:
        limit (int): The upper limit for generating prime numbers.
                     Must be an integer between 2 and MAX_PRIME_LIMIT.

    Returns:
        List[int]: A list of prime numbers up to the given limit.

    Raises:
        TypeError: If `limit` is not an integer.
        ValueError: If `limit` is outside the range [2, MAX_PRIME_LIMIT].
    """
    if not isinstance(limit, int):
       raise TypeError(f"limit must be int, got {type(limit).__name__}")
    if limit < 2:
       return []
    if limit > MAX_PRIME_LIMIT:
       raise ValueError(f"limit must be between 2 and {MAX_PRIME_LIMIT}, got {limit}")




    logger.info("Generating primes up to %d", limit)

    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False

    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    logger.debug("Found %d primes", len(primes))
    return primes
