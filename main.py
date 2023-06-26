from typing import Iterator


def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]


def generate_factors(pool: tuple) -> Iterator:
    n = len(pool)
    indices = [0, 0]
    yield tuple(pool[i] for i in indices)  # this is the first pair
    # Then, change indices to traverse upper triangle of permutations by column
    while indices[0] < n:
        if indices[0] == indices[1]:
            indices[0] = 0
            indices[1] += 1
            yield tuple(pool[i] for i in indices)
        indices[0] += 1
        yield tuple(pool[i] for i in indices)


def find_largest_palindrome():
    pool = tuple(range(999, 100, -1))
    for factors in generate_factors(pool):
        if is_palindrome(factors[0] * factors[1]):
            print(factors[0] * factors[1], factors)
            break


if __name__ == '__main__':
    find_largest_palindrome()
