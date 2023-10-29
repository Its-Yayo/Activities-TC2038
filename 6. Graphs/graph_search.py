#!/usr/bin/python3

from __future__ import annotations

import sys
from typing import Iterator
from collections import deque


Graph = dict[str, list[str]]

g: Graph = {
    'A': ['B', 'C', 'F'],
    'B': ['A', 'D'],
    'C': ['A', 'E', 'F'],
    'D': ['B'],
    'E': ['C', 'F'],
    'F': ['A', 'C', 'E', 'G'],
    'G': ['F']
}


def bfs(start: str, graph: Graph) -> Iterator[str]:
    queue: deque[str] = deque()
    queue.append(start)
    visited: set[str] = {start}

    while queue:
        current: str = queue.popleft()

        if current not in visited:
            yield current
            queue.extend(graph[current])
            visited.add(current)


# FIXME: Update usages
def dfs(start: str, graph: Graph) -> Iterator[str]:
    stack: list[str] = []
    stack.append(start)
    visited: set[str] = {start}

    while stack:
        current: str = stack.pop()

        if current not in visited:
            yield current
            stack.extend(graph[current])
            visited.add(current)


# Implementations for DFS Cycle detection
def dfs_cycle(vertex: str, parent: str, graph: Graph, visited: set) -> Iterator[str]:
    visited.add(vertex)

    for n in graph[vertex]:
        if n not in visited:
            yield from dfs_cycle(n, vertex, graph, visited)
        elif n != parent:
            yield n


# Implementations for BFS Cycle detection
def bfs_cycle(vertex: str, parent: str, graph: Graph, visited: set) -> Iterator[str]:
    queue = deque()

    while queue:
        current: str = queue.popleft()

        if current in visited:
            if parent is not None and current != parent:
                cycle = [vertex]

                while current != vertex:
                    cycle.append(parent)
                    parent = graph[parent]

                cycle.append(vertex)
                yield cycle

        visited.add(current)

        for n in graph[current]:
            if n != parent:
                queue.append((n, current))

def main() -> None:
    print(list(dfs('A', g)))
    print(list(bfs('A', g)))


if __name__ == '__main__':
    main()
    sys.exit(0)




