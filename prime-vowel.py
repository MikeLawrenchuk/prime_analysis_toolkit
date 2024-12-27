from sympy import primerange, factorint
import itertools
import matplotlib.pyplot as plt
import networkx as nx

# Define mapping of primes to vowels (extended to avoid '?')
prime_to_vowel = {
    1: 'A',
    2: 'E',
    3: 'I',
    5: 'O',
    7: 'U'
}

# Fallback vowels to be used for higher primes
fallback_vowels = ['A', 'E', 'I', 'O', 'U']

# Function to generate the vowel representation of a prime number
# Extend this mapping using the corresponding first primes to their 
# respective vowels
def prime_to_vowel_string(primes):
    vowels = []
    for p in primes:
        if p in prime_to_vowel:
            vowels.append(prime_to_vowel[p])
        else:
            # Use fallback vowels in a repeating manner for higher primes
            index = (p % len(fallback_vowels)) - 1
            vowels.append(fallback_vowels[index])
            return vowels

# Generate prime numbers in a range and apply vowel mapping
def generate_vowel_mappings(limit):
    primes = list(primerange(1, limit))  # Generate prime numbers up to 'limit'
    vowel_mappings = prime_to_vowel_string(primes)
    return primes, vowel_mappings

# Define a function to compute composite values and map them to vowel 
representations
# Also define specific mappings for primes like 11 = 'AA' and 13 = 'AI'
def composite_vowel_mapping(primes, vowel_mappings):
    composites = []
    composite_mappings = []
    
    # Special cases for direct prime vowel combinations
    special_prime_mappings = {
        11: 'AA',
        13: 'AI'
    }
    
    # Generate composites by multiplying each pair of primes
    for (p1, v1), (p2, v2) in itertools.combinations(zip(primes, 
    vowel_mappings), 2):
        composite = p1 * p2
        composites.append(composite)
        # Check for special cases
        if composite in special_prime_mappings:
            mapping = special_prime_mappings[composite]
        else:
            # Use the lowercase-uppercase rule for distinguishing factor order
            mapping = v1.lower() + v2.upper() if p1 < p2 else v2.lower() + 
v1.upper()
        composite_mappings.append(mapping)
        return composites, composite_mappings

# Define a visualization of vowel mappings
def visualize_vowel_patterns(primes, vowel_mappings, composites, 
composite_mappings):
    print("Prime Vowel Mapping:")
    for prime, vowel in zip(primes, vowel_mappings):
        print(f"{prime} -> {vowel}")
    
    print("\nComposite Vowel Mapping:")
    for composite, mapping in zip(composites, composite_mappings):
        print(f"{composite} -> {mapping}")

# Plotting the prime and composite relationships using a graph
def plot_vowel_graph(primes, vowel_mappings, composites, composite_mappings):
    G = nx.Graph()
    
    # Add nodes for primes
    for prime, vowel in zip(primes, vowel_mappings):
        G.add_node(prime, label=vowel)
    
    # Add edges for composites
    for (p1, p2), mapping in zip(itertools.combinations(primes, 2), 
    composite_mappings):
        composite = p1 * p2
        edge_style = 'solid'
        edge_color = 'gray'
        edge_width = 1.0
        # Highlight special cases with different styles
        if composite in [11, 13]:
            edge_style = 'dashed'
            edge_color = 'red'
            edge_width = 2.0
        G.add_edge(p1, p2, label=mapping, style=edge_style, 
color=edge_color, width=edge_width)
    
    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')
    edge_labels = nx.get_edge_attributes(G, 'label')
    
    plt.figure(figsize=(10, 8))
    edges = G.edges(data=True)
    # Draw nodes
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=700, 
node_color='skyblue', font_size=10, font_weight='bold')
    # Draw edges with different styles
    for (u, v, d) in edges:
        nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], 
style=d.get('style', 'solid'), edge_color=d.get('color', 'gray'), 
width=d.get('width', 1.0))
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, 
font_color='red')
    plt.title("Prime and Composite Vowel Graph")
    plt.show()

# Function to find the prime factors of a number
def find_prime_factors(number):
    factors = factorint(number)
    print(f"Prime factors of {number}:")
    for prime, power in factors.items():
        print(f"{prime}^{power}")
    return factors

# Main function to execute the exploration
def main():
    limit = 20  # Set limit to generate primes within a range
    primes, vowel_mappings = generate_vowel_mappings(limit)
    composites, composite_mappings = composite_vowel_mapping(primes, 
vowel_mappings)
    visualize_vowel_patterns(primes, vowel_mappings, composites, 
composite_mappings)
    
    # Example of finding prime factors before plotting
    number_to_factor = int(input("Enter a number to find its prime factors: "))
    find_prime_factors(number_to_factor)
    
    # Plot the graph after factoring
    plot_vowel_graph(primes, vowel_mappings, composites, composite_mappings)

if __name__ == "__main__":
    main()
