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

    # Complexity -> O(N^2)
    def __init__(self, values=None) -> None:
        if values is None:
            values = []

        self.__sentinel = OrderedSet.__Node()

        for elem in values:
            self.add(elem)

    # Complexity -> O(N)
    def add(self, value: T) -> None:
        if value in self:
            return

        new_node = OrderedSet.__Node(value)
        new_node.next = self.__sentinel
        new_node.prev = self.__sentinel.prev
        self.__sentinel.prev.next = new_node
        self.__sentinel.prev = new_node

    # Complexity -> O(N)
    def __repr__(self) -> str:
        result: list[T] = []
        current = self.__sentinel.next

        while current != self.__sentinel:
            if current.info is not None:
                result.append(str(current.info))

        return f'OrderedSet({result})'

    # Complexity -> O(N)
    def __contains__(self, value: T) -> bool:
        current = self.__sentinel.next

        while current != self.__sentinel:
            if current.info == value:
                return True
            current = current.next


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
