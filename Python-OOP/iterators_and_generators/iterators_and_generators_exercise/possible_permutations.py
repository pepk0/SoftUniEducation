from itertools import permutations


def possible_permutations(items: list):
    for permutation in permutations(items):
        yield list(permutation)
