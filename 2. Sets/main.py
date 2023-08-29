#!/usr/bin/python3

from __future__ import annotations
import sys
from typing import Generic, TypeVar

T = TypeVar('T')
N = TypeVar('N')


class OrderedSet(Generic[T]):
    # FIXME: Order inherit values for __Node
    class __Node(Generic[N]):
        info: N | None
        next: OrderedSet.__Node[N]
        prev: OrderedSet.__Node[N]

        def __init__(self, value: N | None) -> None:
            self.info = value
            self.next = self
            self.prev = self

    __sentinel: OrderedSet.__Node[T]

    def __init__(self) -> None:
        self.__sentinel = OrderedSet.__Node()

    def add(self, value: T) -> None:
        new_node = OrderedSet.__Node(value)
        new_node.next = self.__sentinel
        new_node.prev = self.__sentinel.prev
        self.__sentinel.prev.next = new_node
        self.__sentinel.prev = new_node

    def __repr__(self) -> str:
        result: list[T] = []
        current = self.__sentinel.next

        while current != self.__sentinel:
            if current.info is not None:
                result.append(str(current.info))


def main() -> None:
    a: OrderedSet[int] = OrderedSet()

    print(a)
    print(f'{hash(a) = :x}')
    print(f'{a is None = }')
    print(f'{a == a = }')
    print(f'{repr(a) = }')


if __name__ == '__main__':
    main()
    sys.exit(1)
