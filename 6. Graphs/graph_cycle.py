#!/usr/bin/env python3

# Lab #6: Graph Cycle Detection
# Solve the graph cycle detection problem using DFS.
#
# @date: 03-Nov-2023
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
from graph_search import dfs_cycle

Graph = dict[str, list[str]]


# TODO: Check implementation!
def has_cycle(initial: str, graph: Graph) -> Optional[list[str]]:
    visited = set()
    
    for vertex in graph:
        if vertex not in visited and dfs_cycle(vertex, None, graph, visited):
            cycle: list = []
            current = initial

            # Loop detected
            while current != initial:
                cycle.append(current)
                current = parent[current]

            cycle.append(vertex)
            cycle.append(initial)

            return cycle
    return None


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

