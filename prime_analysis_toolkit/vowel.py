


#Provides functions for:
#- Mapping primes to vowels
#- Constructing composite vowel mappings
#- Plotting vowel-mapping graphs
#- Factoring integers and plotting factorization graphs

import os
import itertools
import logging
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
from sympy import factorint
from typing import Dict, Tuple, List
from prime_analysis_toolkit.constants import MAX_PRIME_LIMIT
from prime_analysis_toolkit.generators.prime_generator import generate_primes

logger = logging.getLogger(__name__)

if not os.environ.get("DISPLAY"):
    matplotlib.use("Agg")
    logger.info("No DISPLAY found — using non-interactive Agg backend")

FALLBACK_VOWEL = 'X'
LAST_DIGIT_TO_VOWEL = {1: 'A', 3: 'E', 7: 'I', 9: 'O', 2: 'U', 5: 'U'}

def prime_to_vowel_string(primes: List[int]) -> List[str]:
    if any(not isinstance(p, int) or p < 2 for p in primes):
        raise ValueError("All elements in `primes` must be integers ≥ 2.")
    vowels: List[str] = []
    for p in primes:
        ld = p % 10
        vowel = LAST_DIGIT_TO_VOWEL.get(ld, FALLBACK_VOWEL)
        if vowel == FALLBACK_VOWEL:
            logger.warning("No vowel mapping for last digit %d. Using fallback '%s'.", ld, FALLBACK_VOWEL)
        vowels.append(vowel)
    return vowels

def composite_vowel_mapping(primes: List[int], vowels: List[str]) -> Tuple[List[int], List[str]]:
    composites: List[int] = []
    mappings: List[str] = []
    for (p1, v1), (p2, v2) in itertools.combinations(zip(primes, vowels), 2):
        comp = p1 * p2
        composites.append(comp)
        mapping = v1.lower() + v2.upper() if p1 < p2 else v2.lower() + v1.upper()
        mappings.append(mapping)
    return composites, mappings

def generate_vowel_mappings(limit: int) -> Tuple[Dict[int, str], Dict[int, str]]:
    if not isinstance(limit, int) or limit < 2 or limit > MAX_PRIME_LIMIT:
        raise ValueError(f"limit must be int in [2, {MAX_PRIME_LIMIT}], got {limit}")
    logger.info("Generating primes up to %d", limit)
    primes = generate_primes(limit)
    vowels = prime_to_vowel_string(primes)
    prime_map = dict(zip(primes, vowels))
    composites, comp_vowels = composite_vowel_mapping(primes, vowels)
    composite_map = dict(zip(composites, comp_vowels))
    return prime_map, composite_map

def find_prime_factors(number: int) -> Dict[int, int]:
    if not isinstance(number, int) or number < 2:
        logger.error("Factorization Guard: input must be an integer ≥ 2.")
        raise ValueError("Can only factor integers ≥ 2.")
    factors = factorint(number)
    logger.info("Prime factors of %d: %s", number, factors)
    return factors

def plot_vowel_graph(primes: List[int], vowels: List[str], composites: List[int], comp_vowels: List[str], show: bool = True) -> None:
    fig, ax = plt.subplots(figsize=(10, 8))
    G = nx.Graph()
    for prime, vowel in zip(primes, vowels):
        G.add_node(prime, label=vowel)
    for (p1, p2), mapping in zip(itertools.combinations(primes, 2), comp_vowels):
        G.add_edge(p1, p2, label=mapping)
    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw(G, pos, labels=labels, node_size=700, ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
    fig.suptitle("Prime and Composite Vowel Graph")
    fig.tight_layout()
    fig.subplots_adjust(top=0.90)
    output_file = f"vowel_graph_{len(primes)}.png"
    fig.savefig(output_file, dpi=300, bbox_inches="tight")
    logger.info("Saved vowel graph to %s", output_file)
    if show:
        plt.show()
    plt.close(fig)

def plot_factor_graph(number: int, factors: Dict[int, int], show: bool = True) -> None:
    fig, ax = plt.subplots(figsize=(8, 6))
    G = nx.DiGraph()
    G.add_node(number, label=str(number))
    for prime, power in factors.items():
        G.add_node(prime, label=str(prime))
        G.add_edge(number, prime, label=str(power))
    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw(G, pos, labels=labels, node_size=700, ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
    fig.suptitle(f"Factorization Graph for {number}")
    fig.tight_layout()
    fig.subplots_adjust(top=0.88)
    output_file = f"factor_graph_{number}.png"
    fig.savefig(output_file, dpi=300, bbox_inches="tight")
    logger.info("Saved factorization graph to %s", output_file)
    if show:
        plt.show()
    plt.close(fig)
