from prime_analysis_toolkit.analysis.prime_distribution import analyze_distribution
from prime_analysis_toolkit.analysis.prime_distribution import plot_prime_density

def test_analyze_distribution():
    primes = [2, 3, 5, 7, 11, 13]
    result = analyze_distribution(primes)
    assert result is not None  # Ensure some result is returned
    # Add more specific assertions based on the function implementation




def test_plot_prime_density():
    try:
        plot_prime_density(10)  # Test with a small limit
    except Exception as e:
        assert False, f"plot_prime_density raised an exception: {e}"
