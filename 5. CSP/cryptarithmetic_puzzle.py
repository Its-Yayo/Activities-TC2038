#!/usr/bin/python3

# Lab #5: Cryptarithmetic with CSP
# Solve the cryptarithmetic puzzle using a Constraint Satisfaction Problem.
#
# @date: 13-Oct-2023
# @authors:
#           A01754574 Luis Fernando De León Silva
#           A01746999 Luis Eduardo Landeros Hernandez
#
# Repo: https://github.com/Its-Yayo/Activities-TC2038
# Code under free license.
# ----------------------------------------------------------

from __future__ import annotations

import sys

from csp import Constraint, CSP
from typing import Dict, List, Optional, Tuple


def solve_cryptarithmetic_puzzle(addends: list[str], answer: str) -> Optional[dict[str, int]]:

    letters = set("".join(addends + [answer]))
    letters = sorted(letters)

    domains = {letter: list(range(10)) for letter in letters}

    def valid_sum(assignment):
        if len(set(assignment.values())) < len(letters):
            return False

        addend_values = [int("".join([str(assignment[letter]) for letter in addend])) for addend in addends]
        answer_value = int("".join([str(assignment[letter]) for letter in answer]))

        return sum(addend_values) == answer_value

    problem = CSP(letters, domains)
    problem.addConstraint(valid_sum, letters)

    solution = problem.getSolution()

    return solution


def main() -> None:
    result = solve_cryptarithmetic_puzzle(['i', 'luv', 'u'], 'yes')
    print(result)


if __name__ == '__main__':
    main()
    sys.exit(0)
