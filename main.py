from typing import Iterator


def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]


# todo compare speed: this vs itertools
def generate_factors(pool: tuple) -> Iterator:
    indices = [0, 0]
    # Mutate indices to traverse upper triangle of permutations by column
    while indices[1] < len(pool) - 1:
        yield tuple(pool[i] for i in indices)
        if indices[0] == indices[1]:
            indices = [0, indices[1] + 1]  # first row of next column
            yield tuple(pool[i] for i in indices)
        indices[0] += 1


def find_largest_palindrome():
    pool = tuple(range(999, 99, -1))
    largest_palindrome = 0
    largest_factors = (0, 0)
    for factors in generate_factors(pool):
        product = factors[0] * factors[1]
        if product <= largest_palindrome:
            continue
        # todo does the below check improve speed? esp since store factors
        if factors[0] < largest_factors[1]:  # needs to be after the above check
            break
        if is_palindrome(product):
            largest_palindrome = product
            largest_factors = factors
    print(largest_palindrome, largest_factors)


if __name__ == '__main__':
    find_largest_palindrome()
