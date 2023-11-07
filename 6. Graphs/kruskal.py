#!/usr/bin/python3.12

import sys
from heapq import heapify, heappop
from pprint import pprint
from typing import Iterator, Optional, NamedTuple

# FIXME: Fix object type
WeightedGraph = dict[str, set[tuple[str, int]]]


class Edge(NamedTuple):
    weight: int
    u: str
    v: str

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Edge):
            return (self.weight == other.weight
                    and ((self.u == other.u and self.v == other.v)
                    or (self.u == other.v and self.v == other.u)))
        return False

    def __hash__(self) -> int:
        return hash(self.weight) + hash(self.u) + hash(self.v)


def make_heap(graph: WeightedGraph) -> list[Edge]:
    result: set[Edge] = set()
    u: str
    neighbors: set[tuple[str, int]]

    for u, neighbors in graph.items():
        for v, weight in neighbors:
            result.add(Edge(weight, u, v))

    queue: list[Edge] = list(result)
    heapify(queue)

    return result

def add_edge():
    ...

def main() -> None:
    g1: WeightedGraph = {
        'A': {(('B', 4), ('C', 5))},
        'B': {(('A', 4))},
        'C': {(('A', 5), ('D', 6), ('E', 7))},
        'D': {(('C', 6), ('E', 2), ('F', 1))},
        'E': {(('C', 7), ('D', 2), ('F', 3))},
        'F': {(('D', 1), ('E', 3))}
    }

    e1: Edge = Edge(4, 'A', 'B')
    e2: Edge = Edge(4, 'A', 'B')

    s: set[Edge] = set()
    s.add(e1)
    s.add(e2)

    print(s)



if __name__ == '__main__':
    main()
    sys.exit(0)