#!/usr/bin/python3

from dataclasses import dataclass
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


def main() -> None:
    ...


if __name__ == '__main__':
    main()
    sys.exit(0)