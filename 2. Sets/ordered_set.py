#!/usr/bin/python3

# Lab #2: Ordered Set Class
# Ordered set implementation using a doubly linked list.
#
# @date: 17-Sep-2023
# @authors:
#           A01754574 Luis Fernando De León Silva
#           A01746999 Luis Eduardo Landeros Hernandez
#
# Repo: https://github.com/Its-Yayo/Activities-TC2038
# Code under free license.
# ----------------------------------------------------------

from __future__ import annotations
from typing import Generic, TypeVar, cast
from collections.abc import Iterable, Iterator
import sys

T = TypeVar('T')
N = TypeVar('N')
I = TypeVar('I')


class OrderedSet(Generic[T]):

    # FIXME: Order inherit values for __Node
    class __Node(Generic[N]):
        info: N | None
        next: OrderedSet.__Node[N]
        prev: OrderedSet.__Node[N]

        def __init__(self, value: N | None = None) -> None:
            self.info = value
            self.next = self
            self.prev = self

    class __Iterator(Generic[I]):
        __sentinel: OrderedSet.__Node[I]
        __current: OrderedSet.__Node[I]

        # Complexity -> O(1)
        def __init__(self, sentinel: OrderedSet.__Node[I]) -> None:
            self.__sentinel = sentinel
            self.__current = self.__sentinel.next

        # Complexity -> O(1)
        def __iter__(self) -> Iterator[I]:
            return self

        # Complexity -> O(1)
        def __next__(self) -> I:
            if self.__current == self.__sentinel:
                raise StopIteration

            result = cast(I, self.__current.info)
            self.__current = self.__current.next
            return result

    __sentinel: OrderedSet.__Node[T]
    __count: int

    # Complexity -> O(N^2)
    def __init__(self, values: Iterable[T] = []) -> None:
        self.__sentinel = OrderedSet.__Node()
        self.__count = 0

        for elem in values:
            self.add(elem)

    # Complexity -> O(N)
    def add(self, value: T) -> None:
        if value in self:
            return

        self.__count += 1
        new_node = OrderedSet.__Node(value)
        new_node.next = self.__sentinel
        new_node.prev = self.__sentinel.prev
        self.__sentinel.prev.next = new_node
        self.__sentinel.prev = new_node

    # Complexity -> O(N)
    def __repr__(self) -> str:
        if self:
            return f'OrderedSet({list(self)})'
        return 'OrderedSet()'

    # Complexity -> O(N)
    def __contains__(self, value: T) -> bool:
        # current = self.__sentinel.next
        # while current != self.__sentinel:
        #     if current.info == value:
        #         return True
        #     current = current.next
        # return False
        for elem in self:
            if elem == value:
                return True
        return False

    # Complexity -> O(1)
    def __len__(self) -> int:
        return self.__count

    # Complexity -> O(1)
    def __iter__(self) -> Iterator[T]:
        return OrderedSet.__Iterator(self.__sentinel)

    # Complexity -> O(N)
    def discard(self, value: T) -> None:
        current = self.__sentinel.next

        while current != self.__sentinel:
            if current.info == value:
                current.prev.next = current.next
                current.next.prev = current.prev

                return


def main() -> None:
    a: OrderedSet[int] = OrderedSet([4, 8, 15, 16, 23, 42])
    print(a)
    print(f'{hash(a) = :x}')
    print(f'{a is None = }')
    print(f'{a == a = }')
    print(f'{repr(a) = }')
    a.add(4)
    a.add(8)
    a.add(15)
    print(f'{repr(a) = }')
    print(f'{len(a) = }')
    a.add(108)
    print(f'{len(a) = }')
    print(f'{8 in a = }')
    print(f'{5 in a = }')
    b: OrderedSet[str] = OrderedSet()
    print(f'{b = }')
    b.add('hello')
    b.add('bye')
    c = OrderedSet(b)
    c.add('hi')
    print(f'{b = }')
    print(f'{c = }')
    d = OrderedSet('hello world')
    print(f'{d = }')
    e = OrderedSet((5, 6, 7, 9))
    print(f'{e = }')
    f = OrderedSet({'uno': 'one', 'dos': 'two', 'tres': 'three'}.items())
    print(f'{f = }')

if __name__ == '__main__':
    main()
    sys.exit(1)



