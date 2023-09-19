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


def main() -> None:
    print(power_set([]))
    print(power_set(['x']))
    print(power_set(['x', 'y']))
    print(power_set(['x', 'y', 'z']))
    print(power_set(['w', 'x', 'y', 'z']))


if __name__ == '__main__':
    main()
    sys.exit(1)
