from itertools import permutations


def possible_permutations(items: list) -> list:
    for permutation in permutations(items):
        yield list(permutation)
