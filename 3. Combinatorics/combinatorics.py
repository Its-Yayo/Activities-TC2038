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


def main() -> None:
    pprint(sorted_nicely(power_set([])))
    pprint(sorted_nicely(power_set(['x'])))
    pprint(sorted_nicely(power_set(['x', 'y'])))
    pprint(sorted_nicely(power_set(['x', 'y', 'z'])))
    pprint(sorted_nicely(power_set(['w', 'x', 'y', 'z'])))


if __name__ == '__main__':
    main()
    sys.exit(1)
