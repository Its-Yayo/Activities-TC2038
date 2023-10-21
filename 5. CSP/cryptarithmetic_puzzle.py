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
from typing import Dict, List, Optional


class Constraints(Constraint[str, int]):
    def __init__(self, letters: List[str], answer: str, addends: List[str]) -> None:
        super().__init__(letters)
        self.letters = letters
        self.answer = answer
        self.addends = addends

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        if len(set(assignment.values())) < len(assignment):
            return False

        if len(assignment) == len(self.letters):
            cont1 = 0
            cont2 = 0
            cont3 = 0

            for elem in self.addends:
                cont1 = len(elem) - 1
                for e in elem:
                    cont2 += assignment[e] * (10 ** cont1)
                    cont1 -= 1

            cont1 = len(self.answer) - 1
            for e in self.answer:
                cont3 += assignment[e] * (10 ** cont1)
                cont1 -= 1

            return cont2 == cont3

        return True


def solve_cryptarithmetic_puzzle(addends: list[str], answer: str) -> Optional[dict[str, int]]:
    letters = set("".join(addends + [answer]))
    letters = sorted(letters)

    domains = {letter: list(range(10)) for letter in letters}

    problem = CSP(letters, domains)
    problem.add_constraint(Constraints(letters, answer, addends))

    s = problem.backtracking_search()
    solution = {}

    if s:
        for k in s.keys():
            solution[k.upper()] = s[k]
        return solution
    else:
        return None


def main() -> None:
    result = solve_cryptarithmetic_puzzle(['i', 'luv', 'u'], 'yes')
    print(result)


if __name__ == '__main__':
    main()
    sys.exit(0)
