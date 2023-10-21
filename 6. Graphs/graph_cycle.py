#!/usr/bin/env python3

# Lab #6: Graph Cycle Detection
# Solve the graph cycle detection problem using DFS.
#
# @date: 02-Nov-2023
# @authors:
#           A01754574 Luis Fernando De León Silva
#           A01746999 Luis Eduardo Landeros Hernandez
#
# Repo: https://github.com/Its-Yayo/Activities-TC2038
# Code under free license.
# ----------------------------------------------------------

from __future__ import annotations

import sys
from typing import Iterator, Optional

Graph = dict[str, list[str]]


def has_cycle(initial: str, graph: Graph) -> Optional[list[str]]:
    ...


def main() -> None:
    initial = 'A'
    graph: Graph = {
        'A': ['B'],
        'B': ['A', 'D'],
        'C': ['D', 'E'],
        'D': ['C', 'E'],
        'E': ['C', 'D']
    }

    print(has_cycle(initial, graph))


if __name__ == '__main__':
    main()
    sys.exit(0)

