#!/usr/bin/python3

from typing import Iterator, TypeVar, Generic, List, Optional
from collections import deque

Tree = Optional[list[any]]

"""
Tree:
           a
         /   \
        b     c        
       /       \      
      d         e    
               / \
              f   g    
        
"""

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

# def inorder(tree: Tree) -> Iterator[any]:
#     if tree is None:
#         return
#     yield from inorder(tree[1])
#     yield tree[0]
#     yield from inorder(tree[2])

def inorder(root: Tree) -> Iterator[any]:
    if root:



def preorder(tree: Tree) -> Iterator[any]:
    if tree is None:
        return
    yield tree[0]
    yield from preorder(tree[1])
    yield from preorder(tree[2])

