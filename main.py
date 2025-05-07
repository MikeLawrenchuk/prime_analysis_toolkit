#!/usr/bin/env python3
"""
main.py

Unified CLI for:
  - sieve-based prime generation
  - twin-prime generation
  - prime-density plotting
  - vowel-mapping graphs
  - factorization graphs
"""
import os
import argparse
import logging
import matplotlib

if not os.environ.get("DISPLAY"):
    matplotlib.use("Agg")

from prime_analysis_toolkit.generators.prime_generator import generate_primes
from prime_analysis_toolkit.generators.twin_prime_generator import generate_twin_primes
from prime_analysis_toolkit.analysis.prime_distribution import plot_prime_density
from prime_analysis_toolkit.vowel import (
    generate_vowel_mappings,
    plot_vowel_graph,
    find_prime_factors,
    plot_factor_graph,
)


def main():
    parser = argparse.ArgumentParser(prog="prime_analysis_toolkit")
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable debug-level logging"
    )
    subparsers = parser.add_subparsers(dest="cmd")

    p_primes = subparsers.add_parser(
        "primes", help="Generate all primes up to <limit>"
    )
    p_primes.add_argument(
        "limit", type=int, metavar="LIMIT",
        help="Upper bound for prime generation (≥2)"
    )

    p_twin = subparsers.add_parser(
        "twin-primes", help="Generate all twin primes up to <limit>"
    )
    p_twin.add_argument(
        "limit", type=int, metavar="LIMIT",
        help="Upper bound for twin-prime generation (≥2)"
    )

    p_density = subparsers.add_parser(
        "density", help="Plot prime density up to <limit>"
    )
    p_density.add_argument(
        "limit", type=int, metavar="LIMIT",
        help="Upper bound for density plot (≥2)"
    )

    p_vowel = subparsers.add_parser(
        "vowel", help="Produce and save/display the vowel-mapping graph"
    )
    p_vowel.add_argument(
        "limit", type=int, metavar="LIMIT",
        help="Upper bound for vowel mapping (≥2)"
    )
    p_vowel.add_argument(
        "--no-plot", action="store_true",
        help="Skip saving/displaying the vowel graph"
    )
    p_vowel.add_argument(
        "--no-show", action="store_true",
        help="Save graphs but do not pop up windows (headless)"
    )

    p_factor = subparsers.add_parser(
        "factor", help="Factor an integer and save/display its factor graph"
    )
    p_factor.add_argument(
        "number", type=int, metavar="N",
        help="Integer (≥2) to factor"
    )
    p_factor.add_argument(
        "--no-show", action="store_true",
        help="Save graph but do not pop up window"
    )

    args = parser.parse_args()
    if not args.cmd:
        parser.print_help()
        return

    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    logger = logging.getLogger()

    if args.cmd == "primes":
        logger.debug("Generating primes up to %d", args.limit)
        primes = generate_primes(args.limit)
        logger.info("Primes ≤ %d: %s", args.limit, primes)

    elif args.cmd == "twin-primes":
        logger.debug("Generating twin primes up to %d", args.limit)
        twins = generate_twin_primes(args.limit)
        logger.info("Twin primes ≤ %d: %s", args.limit, twins)

    elif args.cmd == "density":
        logger.debug("Plotting prime density up to %d", args.limit)
        plot_prime_density(args.limit)

    elif args.cmd == "vowel":
        logger.debug("Generating vowel mappings up to %d", args.limit)
        prime_map, composite_map = generate_vowel_mappings(args.limit)
        logger.info("Prime→Vowel map: %s", prime_map)
        logger.info("Composite→Vowel map: %s", composite_map)

        if not args.no_plot:
            show = not args.no_show
            logger.debug("Plotting vowel graph (show=%s)", show)
            plot_vowel_graph(
                list(prime_map.keys()),
                list(prime_map.values()),
                list(composite_map.keys()),
                list(composite_map.values()),
                show=show
            )

    elif args.cmd == "factor":
        logger.debug("Factoring %d", args.number)
        factors = find_prime_factors(args.number)
        logger.info("Factors: %s", factors)

        show = not args.no_show
        logger.debug("Plotting factor graph (show=%s)", show)
        plot_factor_graph(args.number, factors, show=show)


if __name__ == "__main__":
    main()
