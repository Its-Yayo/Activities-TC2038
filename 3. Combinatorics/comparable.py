#!/usr/bin/python3

from __future__ import annotations
from typing import Any, Protocol, TypeVar

C = TypeVar('C', bound='Comparable')


class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        ...

    def __lt__(self: C, other: C) -> bool:
        ...

    def __le__(self: C, other: C) -> bool:
        return not other < self

    def __gt__(self: C, other: C) -> bool:
        return other < self

    def __ge__(self: C, other: C) -> bool:
        return not self < other