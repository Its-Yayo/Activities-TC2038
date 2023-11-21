#!/usr/bin/python3

from dataclasses import dataclass
from pprint import pprint
import sys

@dataclass
class Item:
    name: str
    weight: int
    value: int

@dataclass
class Entry:
    value: int
    items: list[Item]


Table = list[list[Entry]]


def solve(size: int, items: list[Item]) -> Table:
    table: Table = [[Entry(0, [])] for _ in range(len(items))]



def main() -> None:
    table: Table = solve(4, [Item('Guitar', 1, 1_500),
                                        Item('Stereo', 4, 3_000),
                                        Item('Laptop', 3, 2_000),
                                        Item('IPhone', 1, 2_000)])

    pprint(table)


if __name__ == '__main__':
    main()
    sys.exit(0)