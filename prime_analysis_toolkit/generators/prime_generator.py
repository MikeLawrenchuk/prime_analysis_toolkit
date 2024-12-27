def generate_primes(limit):
    """
    Generate all prime numbers up to a given limit using the Sieve of Eratosthenes.

    Args:
        limit (int): The upper limit for generating prime numbers.

    Returns:
        list: A list of prime numbers up to the given limit.
    """
    primes = []
    sieve = [True] * (limit + 1)
    for num in range(2, limit + 1):
        if sieve[num]:
            primes.append(num)
            for i in range(num * num, limit + 1, num):
                sieve[i] = False
    return primes

