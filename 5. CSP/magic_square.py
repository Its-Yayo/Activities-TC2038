#!/usr/bin/python3

from abc import ABC
from csp import Constraint, CSP
from typing import NamedTuple, Optional, Dict, List, Tuple
import sys

Grid = List[List[int]]


class GridLocation(NamedTuple):
    row: int
    column: int


def check_square(grid: Grid) -> bool:
    ((a, b, c),
     (d, e, f),
     (g, h, i)) = grid

    return ((a + b + c) == (d + e + f) == (g + h + i)
            == (a + d + g) == (b + e + h) == (c + f + i))


class MagicPurpleConstraint(Constraint[GridLocation, int], ABC):
    def __init__(self, variables: list[int]):
        super().__init__(variables)
        self.variables: list[int] = variables

    def satisfied(self, assignment: dict[GridLocation, int]) -> bool:
        if len(assignment) == len(set(assignment.values())):
            return False

        return True


def main() -> None:
    gl1 = GridLocation(1, 2)
    print(gl1.row)
    print(gl1.column)

    gl2 = GridLocation(1, 2)
    print(gl1 == gl2)

    r, c = gl1
    print(r, c)


if __name__ == '__main__':
    main()
    sys.exit(1)
