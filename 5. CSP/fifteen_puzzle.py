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
from typing import NamedTuple, Optional, Tuple

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
            new_frame = [list(row) for row in frame]
            # Swaps the values of the blank space and the new space
            new_frame[none_row][none_col], new_frame[new_row][new_col] = new_frame[new_row][new_col], \
                new_frame[none_row][none_col]
            new_frame = tuple(tuple(row) for row in new_frame)

            result.append(new_frame)

    return result


# My method
def heuristic(frame: Frame) -> float:
    result: int = 0
    goal_frame = (((1, 2, 3, 4),
                   (5, 6, 7, 8),
                   (9, 10, 11, 12),
                   (13, 14, 15, 0)))

    # Iterate over the frame
    for row in range(0, 4):
        for col in range(0, 4):
            if frame[row][col] != goal_frame[row][col]:
                # Updates heuristic value if the value is out of place
                result += 1

    return float(result)


"""
# Manhattan distance method
def heuristic(frame: Frame) -> float:
    result: int = 0
    goal_row, goal_col = None, None
    goal_frame = (((1, 2, 3, 4),
                   (5, 6, 7, 8),
                   (9, 10, 11, 12),
                   (13, 14, 15, 0)))

    # Iterate over the frame
    for row in range(0, 4):
        for col in range(0, 4):
            if frame[row][col] != 0:
                # Gets the goal row and column of the current value
                goal_row, goal_col = divmod(frame[row][col] - 1, 4)
                result += abs(row - goal_row) + abs(col - goal_col)

    return float(result) """


def goal_test(frame: Frame) -> bool:
    result: bool = True
    goal_frame = (((1, 2, 3, 4),
                   (5, 6, 7, 8),
                   (9, 10, 11, 12),
                   (13, 14, 15, 0)))

    for row in range(0, 4):
        for col in range(0, 4):
            # Checks if the frame is equal or not to the goal frame
            if frame[row][col] != goal_frame[row][col]:
                result = False
                break

    return result


def solve_puzzle(frame: Frame) -> None:
    # Nested function that returns the movement of the blank space of the nodes
    def get_puzzle_movement(current: Frame, parent: Optional[Frame]) -> str:
        for row in range(0, 4):
            for col in range(0, 4):
                if current[row][col] == 0:
                    if current[row][col] != parent[row][col]:
                        # Needs to be the parent value because the current value is 0. Now it worksss
                        value = parent[row][col]

                        if col < 3 and current[row][col + 1] == value:
                            return f"Move {value} right"
                        elif col > 0 and current[row][col - 1] == value:
                            return f"Move {value} left"
                        elif row < 3 and current[row + 1][col] == value:
                            return f"Move {value} down"
                        elif row > 0 and current[row - 1][col] == value:
                            return f"Move {value} up"
        raise ValueError("No movement")

    result: Optional[Node[Frame]] = astar(frame, goal_test, successors, heuristic)

    if result is None:
        print("No solution found!")
        sys.exit(1)
    else:
        path = node_to_path(result)
        steps = len(path) - 1

        print(f"Solution requires {steps} step") if steps == 1 else print(f"Solution requires {steps} steps")

        for step in range(1, len(path)):
            move = get_puzzle_movement(path[step], path[step - 1] if step > 0 else None)
            print(f"Step {step}: {move}")


def main() -> None:
    puzzle = ((2, 3, 4, 8),
              (1, 5, 7, 11),
              (9, 6, 12, 15),
              (13, 14, 10, 0))

    solve_puzzle(puzzle)

    # I needed debugging messages to check if any of the 3 functions were working properly for the puzzle
    """ Debugging successor function
    successor_frames = successors(puzzle)

    for idx, successor_puzzle in enumerate(successor_frames):
        print(f"Successor {idx + 1}:")
        for row in successor_puzzle:
            print(row)
        print() """

    """ Debugging heuristic function 
    print(heuristic(puzzle)) """

    """ Debugging goal_test function 
    print(goal_test(puzzle)) """


if __name__ == "__main__":
    main()
    sys.exit(0)
