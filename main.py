from itertools import combinations_with_replacement
from typing import Iterable

import numpy as np


def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]


def generate_factors() -> Iterable:
    return combinations_with_replacement(np.arange(999, 100, -1), r=2)


def find_largest_palindrome():
    for factors in generate_factors():
        if is_palindrome(factors[0] * factors[1]):
            print(factors[0] * factors[1], factors)
            break


if __name__ == '__main__':
    find_largest_palindrome()
