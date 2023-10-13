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


def main() -> None:
    print(list(bfs('A', g)))


if __name__ == '__main__':
    main()
    sys.exit(0)




