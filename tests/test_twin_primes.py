from prime_analysis_toolkit.generators.twin_prime_generator import generate_twin_primes

def test_generate_twin_primes():
    assert generate_twin_primes(20) == [(3, 5), (5, 7), (11, 13), (17, 
19)]
    assert generate_twin_primes(10) == [(3, 5), (5, 7)]
    assert generate_twin_primes(2) == []
    assert generate_twin_primes(0) == []

