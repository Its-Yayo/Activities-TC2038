#!/usr/bin/python3

import sys
from typing import Optional

from graph import Graph
from generic_search import bfs, node_to_path, Node


def main() -> None:
    metrorrey: Graph[str] = Graph(["Talleres",
                                   "San Bernabe",
                                   "Unidad Modelo",
                                   "Aztlan",
                                   "Peniteniana",
                                   "Alfonso Reyes",
                                   "Miltras",
                                   "Simon Bolivar",
                                   "Hospital",
                                   "Edison",
                                   "Central",
                                   "Sendero",
                                   "Santiago Tapia",
                                   "San Nicholas",
                                   "Anahuac",
                                   "Universidad"
                                   "Ninos Heroes",
                                   "Regina",
                                   "General Anaya",
                                   "Cuauhtemoc",
                                   "Del Golfo",
                                   "Hospital Metropolitano",
                                   "Los Angeles",
                                   "Ruiz Cortines",
                                   "Colonia Moderna",
                                   "Metalurgicos",
                                   "Felix U. Gomez",
                                   "Parque Fundadora",
                                   "Y. Ortega",
                                   "Eloy Cavazos",
                                   "Lerdo de Tejada",
                                   "Exposicion"])

    metrorrey.add_edge_by_vertices("Talleres", "San Bernabe")
    metrorrey.add_edge_by_vertices("San Bernabe", "Unidad Modelo")

    result: Optional[Node[str]] = bfs(
        "Talleres",
        lambda x: x == "Unidad Modelo",
        metrorrey.neighbors_for_vertex
    )

    if result:
        path: list[str] = node_to_path(result)
        print(path)
    else:
        print("No solution found.")


if __name__ == '__main__':
    main()
    sys.exit(0)
