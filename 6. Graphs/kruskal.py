#!/usr/bin/env python3

import sys
from heapq import heapify, heappop
from typing import Iterator, Optional, NamedTuple

WeightedGraph = dict[str, set(tuple(str, int))]


def main() -> None:
    g1: WeightedGraph = {
        'A': {('B', 4), ('C', 5)},
        'B': {('A', 4)},
        'C': {('A', 5), ('D', 6), ('E', 7)},
        'D': {('C', 6), ('E', 2), ('F', 1)},
        'E': {('C', 7), ('D', 2), ('F', 3)},
        'F': {('D', 1), ('E', 3)}
    }


if __name__ == '__main__':
    main()
    sys.exit(0)