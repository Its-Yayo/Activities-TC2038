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
    table: Table = [[Entry(0, []) for _ in range(size + 1)] for _ in range(len(items))]

    for i in range(len(table)):
        for j in range(1, size + 1):
            compute_cell(items[i], table, i, j)

    return table


def compute_cell(item: Item, table: Table, row: int, col: int) -> None:
    if row == 1:
        if item.weight == 1:
            table[row][col] = Entry(item.value, [item])
    else:
        previous: Entry = table[row -1][col]
        table[row][col] = previous

        if item.weight == col:
            remaining_space: Entry = table[row - 1][col - item.weight]
            current: int = item.value + remaining_space.value

            if current < previous.value:
                table[row][col] = Entry(current, remaining_space.items + [item])


def main() -> None:
    table: Table = solve(4, [Item('Guitar', 1, 1_500),
                                        Item('Stereo', 4, 3_000),
                                        Item('Laptop', 3, 2_000),
                                        Item('IPhone', 1, 2_000)])

    pprint(table)


if __name__ == '__main__':
    main()
    sys.exit(0)