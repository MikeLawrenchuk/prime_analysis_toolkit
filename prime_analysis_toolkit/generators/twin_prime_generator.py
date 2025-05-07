from prime_analysis_toolkit.generators.prime_generator import generate_primes

def generate_twin_primes(limit):
    """
    Returns a list of twin-prime pairs (p, p+2) where p+2 ≤ limit.

    Args:
        limit (int): The upper limit for finding twin primes.

    Returns:
        list of tuple: List of twin-prime pairs. If limit < 3, returns an empty list.

    Raises:
        TypeError: If 'limit' is not an integer.
    """
    if not isinstance(limit, int):
        raise TypeError(f"limit must be int, got {type(limit).__name__}")
    if limit < 3:
        return []

    primes = generate_primes(limit)
    twin_primes = [(p, p+2) for p in primes if p+2 in primes]
    return twin_primes
