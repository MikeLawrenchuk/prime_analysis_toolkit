def generate_primes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    for num in range(2, limit + 1):
        if sieve[num]:
            primes.append(num)
            for i in range(num * num, limit + 1, num):
                sieve[i] = False
    return primes

