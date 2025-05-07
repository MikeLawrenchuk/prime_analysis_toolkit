#!/usr/bin/env python3
from prime_analysis_toolkit.generators.prime_generator import generate_primes

def analyze_distribution(data):
    """
    Compute the density π(p)/p for a sequence of primes.

    If `data` is an integer, it is treated as the upper limit
    and all primes ≤ data are generated. If `data` is
    a list or tuple of integers, it is taken to be exactly the
    sequence of primes.

    Returns:
        (primes, densities):  
          * primes    – list of ints  
          * densities – list of floats, where densities[i] = (i+1)/primes[i]
    """
    # Handle integer input by generating primes up to 'limit'
    if isinstance(data, int):
        limit = data
        if limit < 2:
            return [], []
        primes = generate_primes(limit)
    # Handle explicit prime list/tuple input
    elif isinstance(data, (list, tuple)):
        primes = list(data)
        if any((not isinstance(p, int)) or p < 2 for p in primes):
            raise ValueError("All elements must be integers ≥ 2.")
    else:
        raise TypeError("Input must be an int or a list/tuple of ints.")

    # Compute densities π(p)/p for each prime p
    densities = [(i+1) / p for i, p in enumerate(primes)]
    return primes, densities

# alias for backwards compatibility
plot_prime_density = analyze_distribution
