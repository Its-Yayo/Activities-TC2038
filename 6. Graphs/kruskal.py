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

    return queue


def add_edge(graph: WeightedGraph, edge: Edge) -> None:
    weight, u, v = edge
    graph[u].add((v, weight))
    graph[v].add((u, weight))


def remove_edge(graph: WeightedGraph, edge: Edge) -> None:
    weight, u, v = edge
    graph[u].remove((v, weight))
    graph[v].remove((u, weight))


def has_cycle(initial: str, graph: WeightedGraph, visited: Optional[set[str]], parent: Optional[str]) -> bool:
    if visited is None:
        visited = set()
    visited.add(initial)

    for vertex, _ in graph[initial]:
        if vertex in visited:
            if vertex != parent:
                return True

        elif has_cycle(vertex, graph, visited, initial):
            return True

    return False


def kruskal_mst(graph: WeightedGraph) -> tuple[int, WeightedGraph]:
    queue: list[Edge] = make_heap(graph)
    result: WeightedGraph = {k: set for k in graph}
    remaining_edges: int = len(graph) - 1
    total = 0
    visited: set[str] = set()

    while remaining_edges:
        edge: Edge = heappop(queue)
        add_edge(result, edge)

        # FIXME: Args fix
        if edge.u in visited and edge.v in visited and has_cycle(edge.u, result, ):
            remove_edge(result, edge)
        else:
            visited.add(edge.u)
            visited.add(edge.v)

            total += edge.weight
            remaining_edges -= 1

    return (total, result)


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