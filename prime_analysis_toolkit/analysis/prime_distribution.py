import matplotlib.pyplot as plt
from prime_analysis_toolkit.generators.prime_generator import generate_primes

def plot_prime_density(limit):
    primes = generate_primes(limit)
    x = range(1, limit)
    y = [1 if i in primes else 0 for i in x]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, linestyle='None', marker='o', markersize=2)
    plt.xlabel('Number')
    plt.ylabel('Is Prime')
    plt.title(f'Prime Density up to {limit}')
    plt.show()

def analyze_distribution(primes):
    """
    Analyzes the distribution of prime numbers.

    Args:
        primes (list): A list of prime numbers.

    Returns:
        dict: A dictionary with basic statistics about the primes.
    """
    if not primes:
        return {"max_prime": None, "count": 0, "density": 0}
    
    max_prime = max(primes)
    count = len(primes)
    density = count / max_prime if max_prime else 0

    return {"max_prime": max_prime, "count": count, "density": density}
