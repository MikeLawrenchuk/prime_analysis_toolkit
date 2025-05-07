
from prime_analysis_toolkit.generators.prime_generator import generate_primes

def generate_twin_primes(limit):
    """
    Returns a list of twin-prime pairs (p, p+2) where p+2 ≤ limit.

    Args:
        limit (int): The upper limit for finding twin primes. Must be ≥ 3.

    Returns:
        list of tuple: List of twin-prime pairs.

    Raises:
        ValueError: If 'limit' is not an integer ≥ 3.
    """
    # Input validation guard
    if not isinstance(limit, int) or limit < 3:
        raise ValueError("Limit must be an integer ≥ 3 to find twin primes.")

    primes = generate_primes(limit)
    twin_primes = [(p, p+2) for p in primes if p+2 in primes]
    return twin_primes
