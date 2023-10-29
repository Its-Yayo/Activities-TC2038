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
from graph_search import dfs, bfs

Graph = dict[str, list[str]]


# TODO: Implement me!
def get_cycle(current: str, parent: dict[str, str]) -> list[str]:
    ...


# TODO: Implement me!
def has_cycle(initial: str, graph: Graph) -> Optional[list[str]]:
    '''
    visited: set[str] = set()
    stack: list[str] = [initial]
    parent: dict[str, str] = {initial: initial}

    while stack:
        current: str = stack.pop()

        if current in visited:
            return get_cycle(current, parent)

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)
                parent[neighbor] = current

    return None'''
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

