#!/usr/bin/python3

from abc import ABC
from csp import Constraint, CSP
from typing import NamedTuple, Optional, Dict, List, Tuple
from pprint import pprint
import sys

Grid = List[List[int]]


class GridLocation(NamedTuple):
    row: int
    column: int


def check_square(grid: Grid) -> bool:
    ((a, b, c),
     (d, e, f),
     (g, h, i)) = grid

    return ((a + b + c) == (d + e + f) == (g + h + i)  # rows
            == (a + d + g) == (b + e + h) == (c + f + i))  # columns


class MagicPurpleConstraint(Constraint[GridLocation, int], ABC):
    def __init__(self, variables: list[int]):
        super().__init__(variables)
        self.variables: list[int] = variables

    def satisfied(self, assignment: dict[GridLocation, int]) -> bool:
        if len(assignment) != len(set(assignment.values())):
            return False

        if len(assignment) < 9:
            return True

        grid: Grid = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

        for var, (row, col) in assignment.items():
            grid[row][col] = var

        return check_square(grid)


def main() -> None:
    # gl1 = GridLocation(1, 2)
    # print(gl1.row)
    # print(gl1.column)

    # gl2 = GridLocation(1, 2)
    # print(gl1 == gl2)

    # r, c = gl1
    # print(r, c)

    variables: list[GridLocation] = [GridLocation(r, c) for r in range(3) for c in range(3)]
    domains: dict[GridLocation, list[int]] = {var: list(range(1, 10)) for var in variables}
    csp: CSP[GridLocation, int] = CSP(variables, domains)

    csp.add_constraint(MagicPurpleConstraint(variables))
    solution: Optional[Dict[GridLocation, int]] = csp.backtracking_search()


if __name__ == '__main__':
    main()
    sys.exit(1)
