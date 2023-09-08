#!/usr/bin/python3

from collections.abc import Iterable, Iterator
import sys
def example() -> Iterator[int]:
    for i in range(10):
        yield i

def main() -> None:
    for i in example():
        print(i)

if __name__ == '__main__':
    main()
    sys.exit(1)