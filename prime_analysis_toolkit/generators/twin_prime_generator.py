from prime_analysis_toolkit.generators.prime_generator import generate_primes

def generate_twin_primes(limit):
    primes = generate_primes(limit)
    twins = [(p, p + 2) for p in primes if p + 2 in primes]
    return twins

