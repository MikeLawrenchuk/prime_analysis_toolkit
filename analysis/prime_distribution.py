import matplotlib.pyplot as plt
from generators.prime_generator import generate_primes

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

