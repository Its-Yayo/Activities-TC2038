#!/usr/bin/python3

""" Instructions:
Write in Python or pseudocode a function called heap_children.
The function takes as input a list a containing a binary heap
and an index i. It returns a tuple with the values of the left
and right children corresponding to the element in the a[i].
The tuple should contain None in place of the value of a
non-existing child. Usage example:

>>> heap: list[int] = [1, 3, 6, 5, 9, 8]
>>> heap_children(heap, 1)
(5, 9)
>>> heap_children(heap, 2)
(8, None) """


import sys
from typing import Optional, List, Tuple

def heap_children(a: list[int], i: int) -> tuple[Optional[int], Optional[int]]:
    left_index = (2 * i) + 1
    right_index = (2 * i) + 2

    left_nodes = (a[left_index] if left_index < len(a) else None)
    right_nodes = (a[right_index] if right_index < len(a) else None)

    return left_nodes, right_nodes


def main() -> None:
    heap: list[int] = [1, 3, 6, 5, 9, 8]
    print(heap_children(heap, 0))
    print(heap_children(heap, 1))
    print(heap_children(heap, 2))

if __name__ == '__main__':
    main()
    sys.exit(0)
