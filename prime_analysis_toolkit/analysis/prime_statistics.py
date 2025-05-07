
import statistics
from typing import List, Tuple, Dict, Union


def analyze_distribution(primes: List[int]) -> Dict[str, Union[int, float, None]]:
    """
    Compute statistical metrics for a sequence of prime numbers.

    Args:
        primes (List[int]): Sorted list of prime numbers (each ≥ 2).

    Returns:
        Dict[str, Union[int, float, None]]: A dictionary with the following keys:
            - 'count': int, total number of primes
            - 'min_prime': int, smallest prime in list
            - 'max_prime': int, largest prime in list
            - 'density': float, count / max_prime
            - 'avg_gap': float, average difference between consecutive primes
            - 'gap_variance': float, variance of the gaps between primes

    Raises:
        TypeError: If 'primes' is not a list or tuple.
        ValueError: If any element in 'primes' is not an integer ≥ 2.
    """
    # Guards
    if not isinstance(primes, (list, tuple)):
        raise TypeError("`primes` must be a list or tuple of integers.")
    if not primes:
        return {
            'count': 0,
            'min_prime': None,
            'max_prime': None,
            'density': 0,
            'avg_gap': None,
            'gap_variance': None
        }
    if any(not isinstance(p, int) or p < 2 for p in primes):
        raise ValueError("All elements in `primes` must be integers ≥ 2.")

    # Ensure sorted order
    primes = sorted(primes)

    # Basic statistics
    count = len(primes)
    min_prime = primes[0]
    max_prime = primes[-1]
    density = count / max_prime

    # Gap analysis
    gaps = [j - i for i, j in zip(primes, primes[1:])]
    avg_gap = sum(gaps) / len(gaps) if gaps else 0
    gap_variance = statistics.pvariance(gaps) if len(gaps) > 1 else 0

    return {
        'count': count,
        'min_prime': min_prime,
        'max_prime': max_prime,
        'density': density,
        'avg_gap': avg_gap,
        'gap_variance': gap_variance
    }
