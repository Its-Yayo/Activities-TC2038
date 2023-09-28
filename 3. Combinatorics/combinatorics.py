#!/usr/bin/python3

# Lab #3: Combinatorics
# Combinatorics and Permutations
#
# @date: 29-Sep-2023
# @authors:
#           A01754574 Luis Fernando De León Silva
#           A01746999 Luis Eduardo Landeros Hernandez
#
# Repo: https://github.com/Its-Yayo/Activities-TC2038
# Code under free license.
# ----------------------------------------------------------


from comparable import C
from typing import List, Tuple, TypeVar
from pprint import pprint
import sys


def power_set(s: list[C]) -> list[list[C]]:
    if s:
        r = power_set(s[:-1])
        return r + [subset + [s[-1]] for subset in r]
    else:
        return [[]]


def sorted_nicely(s: list[list[C]]) -> list[list[C]]:
    def size_and_content(subset: list[C]) -> Tuple[int, list[C]]:
        return len(subset), subset

    return sorted(s, key=size_and_content)


def combinations(s: list[C], k: int) -> list[list[C]]:
    return [subset for subset in power_set(s) if len(subset) == k]


def insert(k: C, s: list[C], i: int) -> list[C]:
    return s[:i] + [k] + s[i:]


def insert_everywhere(k: C, s: list[C]) -> list[list[C]]:
    return [insert(k, s, i) for i in range(len(s) + 1)]


def permute(s: list[C]) -> list[list[C]]:
    if s:
        return sum([insert_everywhere(s[0], p) for p in permute(s[1:])], [])
    else:
        return [[]]


def permutations(s: list[C], k: int) -> list[list[C]]:
    return sum([permute(t) for t in combinations(s, k)], [])


# FIXME: Usages still not tested.
def permutations_with_repetitions(s: list[C], k: int) -> list[list[C]]:
    result = []

    def permute_with_repetitions(s: list[C], k: int, p: list[C]) -> None:
        if k == 0:
            result.append(p)
        else:
            for elem in s:
                permute_with_repetitions(s, k - 1, p + [elem])

    permute_with_repetitions(s, k, [])
    return result


def combinations_with_repetitions(s: list[C], k: int) -> list[list[C]]:
    ...


def main() -> None:
    pprint(sorted_nicely(power_set([])))
    pprint(sorted_nicely(power_set(['x'])))
    pprint(sorted_nicely(power_set(['x', 'y'])))
    pprint(sorted_nicely(power_set(['x', 'y', 'z'])))
    pprint(sorted_nicely(power_set(['w', 'x', 'y', 'z'])))

    pprint(sorted_nicely(combinations(['x', 'y', 'z'], 0)))
    pprint(sorted_nicely(combinations(['x', 'y', 'z'], 1)))
    pprint(sorted_nicely(combinations(['x', 'y', 'z'], 2)))

    pprint(insert('x', ['y', 'z'], 0))

    pprint(insert_everywhere('x', ['y', 'z']))

    pprint(permute([[]]))
    pprint(permute(['X']))
    pprint(permute(['X', 'Y']))
    pprint(permute(['X', 'Y', 'Z']))

    pprint(sorted_nicely(permutations(['x', 'y', 'z'], 2)))

    pprint(sorted_nicely(permutations_with_repetitions(['w', 'x', 'y', 'z'], 2)))


if __name__ == '__main__':
    main()
    sys.exit(1)
