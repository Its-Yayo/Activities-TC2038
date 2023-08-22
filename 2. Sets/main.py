#!/usr/bin/python3

import sys 
from typing import Generic, TypeVar

T = TypeVar('T')

class OrderedSet(Generic[T]):
    ...

def main() -> None:
    ordered_set: OrderedSet[int] = OrderedSet()
    pass

if __name__ == '__main__':
    main()
    sys.exit(1)