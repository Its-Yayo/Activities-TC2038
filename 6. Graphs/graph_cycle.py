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
from graph_search import dfs_cycle

Graph = dict[str, list[str]]


# Note: It uses the cycled dfs implementation in graph_search.py file!
# FIXME : Check the dfs_cycle function
def has_cycle(initial: str, graph: Dict[str, List[str]]) -> Optional[List[str]]:
    visited = set()
    parent_dict = {}  # Dictionary to keep track of the parent of each vertex

    for vertex in graph:
        if vertex not in visited:
            # Method called from graph_search.py
            result = dfs_cycle(vertex, None, graph, visited, parent_dict)
            if result is not None:
                return result

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

