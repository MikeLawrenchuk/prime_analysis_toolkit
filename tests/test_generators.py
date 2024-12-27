from prime_analysis_toolkit.generators.prime_generator import generate_primes

def test_generate_primes():
    assert generate_primes(10) == [2, 3, 5, 7]
    assert generate_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert generate_primes(1) == []
    assert generate_primes(2) == [2]
