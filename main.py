from itertools import combinations_with_replacement


def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]


def generate_factors(pool):
    return combinations_with_replacement(pool, 2)


def find_largest_palindrome(max_factor: int, min_factor: int):
    def make_pool(maximum: int) -> range:
        return range(maximum, min_factor - 1, -1)

    pool = make_pool(max_factor)
    largest_palindrome = 0
    largest_factors = (0, 0)
    for factors in generate_factors(pool):
        product = factors[0] * factors[1]
        if product <= largest_palindrome:
            continue
        if is_palindrome(product):
            largest_palindrome = product
            largest_factors = factors
            pool = make_pool(factors[0] - 1)
    return largest_palindrome, largest_factors


if __name__ == '__main__':
    print(find_largest_palindrome(999, 100))
