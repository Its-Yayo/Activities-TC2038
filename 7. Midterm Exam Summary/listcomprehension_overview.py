#!/usr/bin/python3

import sys

def foo(n: int) -> list[int]:
    return [x for x in range(1, n + 1) if n % x == 0]

def main() -> None:
    print(foo(19))
    print(foo(20))

if __name__ == '__main__':
    main()
    sys.exit(0)

