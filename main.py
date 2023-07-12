from itertools import combinations_with_replacement


def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]


def generate_factors(pool):
    return combinations_with_replacement(pool, 2)


def find_largest_palindrome(max_factor: int, min_factor: int):
    largest_palindrome = 0
    for factors in generate_factors(range(max_factor, min_factor - 1, -1)):
        product = factors[0] * factors[1]
        if product <= largest_palindrome:
            continue
        if is_palindrome(product):
            largest_palindrome = product
    return largest_palindrome


if __name__ == '__main__':
    print(find_largest_palindrome(999, 100))
