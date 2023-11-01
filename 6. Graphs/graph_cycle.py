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
from typing import Iterator, Optional, Dict, List

Graph = Dict[str, List[str]]


# Implementations for DFS Cycle detection
def dfs_cycle(vertex: str, graph: Dict[str, List[str]], visited: set, parent_dict: Dict[str, str]) -> Optional[List[str]]:
    visited.add(vertex)

    for n in graph[vertex]:
        if n not in visited:
            parent_dict[n] = vertex
            result = dfs_cycle(n, graph, visited, parent_dict)

            if result is not None:
                return result

        elif parent_dict.get(vertex) is not None and n != parent_dict[vertex]:
            cycle = [n]
            current = vertex

            while current != n:
                cycle.append(current)
                current = parent_dict[current]
            cycle.append(n)
            return cycle

    return None


# Note: It uses the cycled dfs implementation in graph_search.py file!
def has_cycle(initial: str, graph: Graph) -> Optional[List[str]]:
    visited = set()
    parent_dict = {}  # Dictionary to keep track of the parent of each vertex
    result = dfs_cycle(initial, graph, visited, parent_dict)

    if result is not None:
        return result[::-1]

    for vertex in graph:
        if vertex not in visited:
            result = dfs_cycle(vertex, graph, visited, parent_dict)
            if result is not None:
                return result[::-1]

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

