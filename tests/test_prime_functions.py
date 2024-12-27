from prime_analysis_toolkit.generators.prime_generator import generate_primes

def test_generate_primes():
    assert generate_primes(10) == [2, 3, 5, 7]

