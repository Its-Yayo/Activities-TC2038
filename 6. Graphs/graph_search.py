#!/usr/bin/env python3

from __future__ import annotations

import sys
from typing import Iterator, Dict, List, Optional
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
def dfs_cycle(vertex: str, parent: str, graph: Dict[str, List[str]], visited: set, parent_dict: Dict[str, str]) -> Optional[List[str]]:
    visited.add(vertex)

    for n in graph[vertex]:
        if n not in visited:
            parent_dict[n] = vertex
            result = dfs_cycle(n, vertex, graph, visited, parent_dict)

            if result is not None:
                return result
        elif n != parent and parent_dict.get(vertex) != n:
            cycle = [n]
            current = vertex

            while current != n:
                cycle.append(current)
                current = parent_dict[current]
            cycle.append(n)
            return cycle

    return None


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

    return None

def main() -> None:
    print(list(dfs('A', g)))
    print(list(bfs('A', g)))


if __name__ == '__main__':
    main()
    sys.exit(0)




