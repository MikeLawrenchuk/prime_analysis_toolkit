# Prime Analysis Toolkit

A unified Python-based command‑line interface and library for prime number generation, analysis, and visualization. Whether you need raw prime lists, twin primes, density plots, vowel‑mapping graphs, or factorization graphs, this toolkit has you covered.

---

## Features

* **Primes**: Generate all primes up to a specified limit using a fast Sieve of Eratosthenes.
* **Twin Primes**: Identify all twin-prime pairs up to a given limit.
* **Density Plot**: Visualize prime density across the integer range with Matplotlib.
* **Vowel Mapping**: Map primes to vowels based on last digit, build composite mappings, and render/save a comprehensive graph.
* **Factor Graph**: Factor any integer ≥ 2 into its prime factors and produce a directed graph of the factorization.
* **Flexible Output**: Control plotting and display with `--no-plot` and `--no-show` flags.
* **Verbose Logging**: Enable detailed debug output with `-v` or `--verbose`.

---

## Installation

Ensure you have Python 3.8+ and a virtual environment set up.

```bash
git clone https://github.com/your-username/prime_analysis_toolkit.git
cd prime_analysis_toolkit
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

This will install dependencies (`sympy`, `networkx`, `matplotlib`) and register the `prime_analysis_toolkit` command.

---

## Usage

All functionality is accessed via sub-commands. Run the tool without arguments to see the help screen:

```bash
prime_analysis_toolkit
```

### Generate Primes

```bash
prime_analysis_toolkit primes <limit>
# e.g.
prime_analysis_toolkit primes 100
```

### Generate Twin Primes

```bash
prime_analysis_toolkit twin-primes <limit>
# e.g.
prime_analysis_toolkit twin-primes 100
```

### Plot Prime Density

```bash
prime_analysis_toolkit density <limit>
# e.g.
prime_analysis_toolkit density 1000
```

### Vowel‑Mapping Graph

```bash
prime_analysis_toolkit vowel <limit> [--no-plot] [--no-show]
# e.g.
prime_analysis_toolkit vowel 20
prime_analysis_toolkit vowel 20 --no-show
```

### Factorization Graph

```bash
prime_analysis_toolkit factor <number> [--no-show]
# e.g.
prime_analysis_toolkit factor 1234567890
prime_analysis_toolkit factor 1234567890 --no-show
```

### Common Flags

* `-v, --verbose`  : Enable debug-level logging.
* `--no-plot`      : Do not save or display the vowel graph.
* `--no-show`      : Save graphs to disk but skip interactive display (useful in headless environments).

---

## Running Tests

This project uses pytest for unit testing. To run all tests:

```bash
pytest
```

Ensure your virtual environment is active and dependencies are installed.

---

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/my-feature`.
3. Make your changes, add tests, and ensure formatting with `black`.
4. Run `pytest` to confirm all tests pass.
5. Submit a pull request with a clear description.

We welcome bug fixes, new features, and improvements!

---

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.
