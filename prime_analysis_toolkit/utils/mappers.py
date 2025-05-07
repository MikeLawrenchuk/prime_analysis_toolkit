

import logging
from typing import Any, Dict, Iterable, List, Union

# Utility to extract digits in any base

def digits_in_base(n: int, base: int) -> List[int]:
    """
    Return the digits of n in the specified base (most significant first).

    Args:
        n (int): The number to convert. Must be >= 0.
        base (int): The base for conversion (>= 2).

    Returns:
        List[int]: Digits of n in the given base.

    Raises:
        ValueError: If n < 0 or base < 2.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Number must be a non-negative integer.")
    if not isinstance(base, int) or base < 2:
        raise ValueError("Base must be an integer >= 2.")

    if n == 0:
        return [0]

    digits: List[int] = []
    while n > 0:
        n, rem = divmod(n, base)
        digits.append(rem)
    return digits[::-1]


class BaseMapper:
    """
    A generic digit-to-symbol mapper for any base.

    Attributes:
        mapping (Dict[Any, str]): Maps digit values to symbols.
        fallback (str): Symbol for unmapped digits.
    """
    def __init__(self, mapping: Dict[Any, str], fallback: str = 'X'):
        self.mapping = mapping
        self.fallback = fallback

    def map_digit(self, digit: Any) -> str:
        """
        Map a single digit to its symbol, using fallback if not found.
        """
        symbol = self.mapping.get(digit)
        if symbol is None:
            logging.warning(f"No symbol mapping for digit {digit}. Using fallback '{self.fallback}'.")
            return self.fallback
        return symbol

    def map_sequence(self, sequence: Iterable[Any]) -> List[str]:
        """
        Map a sequence of digits to their corresponding symbols.

        Args:
            sequence (Iterable[Any]): Digit values to map.

        Returns:
            List[str]: List of mapped symbols.
        """
        return [self.map_digit(d) for d in sequence]
```

# How to use:
```python
# Pre-defined decimal last-digit mapper
decimal_mapper = BaseMapper({1:'A', 3:'E', 7:'I', 9:'O', 2:'U', 5:'U'}, fallback='X')

# Example usage
digits = digits_in_base(37, 10)  # [3, 7]
symbols = decimal_mapper.map_sequence(digits)  # ['E', 'I']
# For last-digit only
symbol = decimal_mapper.map_digit(digits[-1])  # 'I'
