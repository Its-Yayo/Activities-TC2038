#!/usr/bin/python3

import sys
from typing import Optional

from graph import Graph
from generic_search import bfs, node_to_path, Node


def main() -> None:
    metrorrey: Graph[str] = Graph(["Talleres,"
                                   "San Bernabe",
                                   "Unidad Modelo"])

    metrorrey.add_edge_by_vertices("Talleres", "San Bernabe")
    metrorrey.add_edge_by_vertices("San Bernabe", "Unidad Modelo")


if __name__ == '__main__':
    main()
    sys.exit(0)
