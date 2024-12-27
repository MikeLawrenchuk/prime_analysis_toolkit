import argparse
from prime_analysis_toolkit.generators.prime_generator import generate_primes
from prime_analysis_toolkit.generators.twin_prime_generator import generate_twin_primes
from prime_analysis_toolkit.analysis.prime_distribution import plot_prime_density


def main():
    # Initialize the Argument Parser
    parser = argparse.ArgumentParser(description="Prime Analysis Toolkit")

    # Adding command-line arguments
    parser.add_argument('--generate-primes', type=int, help="Generate all primes up to the given number")
    parser.add_argument('--generate-twin-primes', type=int, help="Generate all twin primes up to the given number")
    parser.add_argument('--plot-prime-density', type=int, help="Plot prime density up to the given number")

    # Parse the arguments
    args = parser.parse_args()

    # Implementing the functionality based on the parsed arguments
    if args.generate_primes:
        primes = generate_primes(args.generate_primes)
        print(f"Primes up to {args.generate_primes}: {primes}")

    if args.generate_twin_primes:
        twin_primes = generate_twin_primes(args.generate_twin_primes)
        print(f"Twin primes up to {args.generate_twin_primes}: {twin_primes}")

    if args.plot_prime_density:
        plot_prime_density(args.plot_prime_density)

if __name__ == "__main__":
    main()


