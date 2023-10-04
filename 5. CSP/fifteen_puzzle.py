#!/usr/bin/python3

# Lab #4: Fifteen Puzzle
# Solve the Fifteen Puzzle using a Constraint Satisfaction Problem
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
from pprint import pprint

from csp import Constraint, CSP
from generic_search import astar, Node, node_to_path

Frame = tuple[tuple[int, ...], ...]


def goal_test(frame: Frame) -> bool:
    ...


def successors(frame: Frame) -> list[Frame]:
    ...


def heuristic(frame: Frame) -> float:
    ...


def solve_puzzle(frame: Frame) -> None:
    result: Optional[Node[Frame]] = astar(
        frame, goal_test, successors, heuristic)
    ...
