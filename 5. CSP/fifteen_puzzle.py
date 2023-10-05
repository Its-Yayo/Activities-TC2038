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

    # Possible movements in up, down, left, right
    moves: list[frame] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    ## Iterate over possible movements
    for move in moves:
        new_row, new_col = none_row + move[0], none_col + move[1]

        if 0 <= new_row < 4 and 0 <= new_col < 4:
            new_frame: Frame = tuple(tuple(row) for row in frame)
            new_frame[none_row][none_col], new_frame[new_row][new_col] = new_frame[new_row][new_col], \
                new_frame[none_row][none_col]
            result.append(new_frame)

    return result


"""
# My method
def heuristic(frame: Frame) -> float:
    result: int = 0
    goal_frame = ((1, 2, 3, 4,
                   5, 6, 7, 8,
                   9, 10, 11, 12,
                   13, 14, 15, 0),)

    # Iterate over the frame
    for row in range(0, 4):
        for col in range(0, 4):
            if frame[row][col] != goal_frame[row][col]:
                # Updates heuristic value if the value is out of place
                result += 1

    return float(result) """


# Manhattan distance method
def heuristic(frame: Frame) -> float:
    result: int = 0

    # Iterate over the frame
    for row in range(0, 4):
        for col in range(0, 4):
            if frame[row][col] != 0:
                result += abs(row - (frame[row][col] - 1) // 4) + abs(col - (frame[row][col] - 1) % 4)

    return float(result)


def goal_test(frame: Frame) -> bool:
    result: bool = True
    goal_frame = ((1, 2, 3, 4,
                   5, 6, 7, 8,
                   9, 10, 11, 12,
                   13, 14, 15, 0),)

    for row in range(0, 4):
        for col in range(0, 4):
            # Checks if the frame is equal or not to the goal frame
            if frame[row][col] != goal_frame[row][col]:
                result = False
                break

    return result


def solve_puzzle(frame: Frame) -> None:
    # Nested function that returns the movement of the blank space of the nodes
    def get_puzzle_movement(node: Node[frame]) -> str:
        current = node.state
        parent = node.parent.state

        for row in range(0, 4):
            for col in range(0, 4):
                if current[row][col] != parent[row][col]:
                    value = current[row][col]

                    if value == parent[row][col]:
                        ...

    result: Optional[Node[Frame]] = astar(frame, goal_test, successors, heuristic)


def main() -> None:
    puzzle = ((2, 3, 4, 8),
              (1, 5, 7, 11),
              (9, 6, 12, 15),
              (13, 14, 10, 0),)

    solve_puzzle(puzzle)


if __name__ == "__main__":
    main()
    sys.exit(1)
