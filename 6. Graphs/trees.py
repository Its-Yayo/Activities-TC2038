#!/usr/bin/python3

from typing import Iterator, TypeVar, Generic, List, Optional
from collections import deque
import sys

Tree = Optional[list[any]]

"""  t: Tree = 
                   a
                 /   \
                b     c        
               /       \      
              d         e    
                       / \
                      f   g    """

t: Tree = \
    ['a',
     ['b',
      ['d', None, None],
      None
      ],
     ['c',
      None,
      ['e',
       ['f', None, None],
       ['g', None, None]
       ]
      ]
     ]


# Inorder: d, b, a, c, f, e, g -> left, root, right
# Preorder: a, b, d, c, e, f, g -> root, left, right
# Postorder: d, b, f, g, e, c, a -> left, right, root
# Level-order: a, b, c, d, e, f, g -> root, left, right

# def inorder(tree: Tree) -> Iterator[any]:
#     if tree:
#       yield from inorder(tree[1])
#       yield tree[0]
#       yield from inorder(tree[2])

def inorder(root: Tree) -> Iterator[any]:
    if root:
        value, left, right = root
        yield from inorder(left)
        yield value
        yield from inorder(right)


def preorder(root: Tree) -> Iterator[any]:
    if root:
        value, left, right = root
        yield value
        yield from preorder(left)
        yield from preorder(right)


def postorder(root: Tree) -> Iterator[any]:
    if root:
        value, left, right = root
        yield from postorder(left)
        yield from postorder(right)
        yield value


def levelorder(root: Tree) -> Iterator[any]:
    queue: deque[Tree] = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        if node:
            current = queue.popleft()

            if current:
                value, left, right = current
                yield value
                queue.append(left)
                queue.append(right)


def main() -> None:
    print(list(inorder(t)))
    print(list(preorder(t)))
    print(list(postorder(t)))


if __name__ == '__main__':
    main()
    sys.exit(1)
