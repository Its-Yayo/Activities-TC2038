#!/usr/bin/python3

from heapq import heappush, heappop
import sys


def heap_sort(data: list[int]) -> list[int]:
    heap: list[int] = []
    for elem in data:
        heappush(heap, elem)
    result: list[int] = []

    while heap:
        result.append(heappop(heap))
    return result


def main() -> None:
    print(heap_sort([7, 2, 5, 1, 9, 3, 6, 4, 8]))


if __name__ == '__main__':
    main()
    sys.exit(1)
