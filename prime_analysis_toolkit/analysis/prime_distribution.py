
import matplotlib.pyplot as plt
from prime_analysis_toolkit.generators.prime_generator import generate_primes


def plot_prime_density(limit):
    """
    Plot the density of primes π(n)/n for all n ≤ limit.

    Args:
        limit (int): The upper limit for calculating prime density. Must be ≥ 2.

    Raises:
        ValueError: If 'limit' is not an integer ≥ 2.
    """
    # Input guard
    if not isinstance(limit, int) or limit < 2:
        raise ValueError("Limit must be an integer ≥ 2 to plot prime density.")

    # Efficient single-pass sieve with running prime count
    sieve = [True] * (limit + 1)
    count = 0
    xs, ys = [], []
    for i in range(2, limit + 1):
        if sieve[i]:
            count += 1
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
        xs.append(i)
        ys.append(count / i)

    # Plotting
    plt.figure(figsize=(8, 5))
    plt.plot(xs, ys)
    plt.xlabel("n")
    plt.ylabel("Prime Density π(n)/n")
    plt.title(f"Prime Density vs n (up to {limit})")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
