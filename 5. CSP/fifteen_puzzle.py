#!/usr/bin/python3

# Lab #4: Fifteen Puzzle
# Solve the Fifteen Puzzle using a Constraint Satisfaction Problem. Every solution should be found in 16 moves or less.
#
# @date: 06-Oct-2023
# @authors:
#           A01754574 Luis Fernando De León Silva
#           A01746999 Luis Eduardo Landeros Hernandez
#
# Repo: https://github.com/Its-Yayo/Activities-TC2038
# Code under free license.
# ----------------------------------------------------------

from __future__ import annotations

import sys
from abc import ABC
from typing import NamedTuple, Optional

from csp import Constraint, CSP
from generic_search import astar, Node, node_to_path

Frame = tuple[tuple[int, ...], ...]


def successors(frame: Frame) -> list[Frame]:
    result: list[Frame] = []
    none_col, none_row = None, None
    new_col, new_row = None, None

    for row in range(0, 4):
        for col in range(0, 4):
            if frame[row][col] == 0:
                none_col, none_row = col, row
                break

    # Possible movements
    moves: list[frame] = [(1, 0), (-1, 0), (0, 1), (0, -1)]



    return result


def heuristic(frame: Frame) -> float:
    ...


def goal_test(frame: Frame) -> bool:
    ...


def solve_puzzle(frame: Frame) -> None:
    result: Optional[Node[Frame]] = astar(frame, goal_test, successors, heuristic)
    ...


def main() -> None:
    puzzle = ((2, 3, 4, 8),
              (1, 5, 7, 11),
              (9, 6, 12, 15),
              (13, 14, 10, 0),)

    solve_puzzle(puzzle)


if __name__ == "__main__":
    main()
    sys.exit(1)
