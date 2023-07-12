from itertools import combinations_with_replacement


def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]


def generate_factors(pool):
    return combinations_with_replacement(pool, 2)


def make_pool(maximum: int, minimum: int) -> range:
    if maximum < minimum:
        maximum = minimum
    return range(maximum, minimum, -1)


def find_palindrome_in_pool(pool: range, largest_palindrome: int, i: int):
    for factors in generate_factors(pool):
        i += 1
        product = factors[0] * factors[1]
        if product <= largest_palindrome:
            continue
        if is_palindrome(product):
            return product, factors[0], i
    else:
        return largest_palindrome, None, i


def find_largest_palindrome(max_factor: int, min_factor: int):
    min_factor -= 1
    largest_palindrome = 0
    pool = make_pool(max_factor, min_factor)
    i = 0
    while pool:
        largest_palindrome, factor, i = find_palindrome_in_pool(pool, largest_palindrome, i)
        if not factor:
            return largest_palindrome, i
        pool = make_pool(factor - 1, min_factor)


if __name__ == '__main__':
    print(find_largest_palindrome(999, 100))
