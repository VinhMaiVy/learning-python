#!/bin/python3

"""
Sorted Treap

Input:
6
12
4
5
3
8
7

Output:
12.0
8.0
5.0
4.5
5.0
6.0

"""

import os
import sys
import math

from random import random


class TreapNode:

    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.priority = random()
        self.cnt = 1
        self.size = 1
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return str((self.key, self.priority, self.size))

    def __str__(self):
        return str((self.key))

    def size(self, node):
        if node is not None:
            return node.size

    def upd_cnt(self):
        self.size = 1 + self.size(self.left) + self.size(self.right)

    def inc_parent_size(self, node):
        if node.parent:
            node.parent.size += 1
            self.inc_parent_size(node.parent)

    def decr_parent_size(self, node):
        if node.parent:
            node.parent.size -= 1
            self.decr_parent_size(node.parent)


class Treap:

    def __init__(self):
        self.root = None

    def __repr__(self):
        lines = []
        nodes = [(self.root, 0)]
        while nodes:
            node, indent = nodes.pop()
            if node is None:
                lines.append('   ' * indent + '*')
            else:
                for _ in range(node.cnt):
                    lines.append('   ' * indent + str(node))
                nodes.append((node.right, indent + 1))
                nodes.append((node.left, indent + 1))
        return "\n".join(lines)

    def _str(self, node):
        res = self._str(node.left) if (node.left is not None) else ''
        for _ in range(node.cnt):
            res += str(node.key) + ' '
        res += self._str(node.right) if (node.right is not None) else ''
        return res

    def __str__(self):
        return self._str(self.root)

    def __len__(self):
        return self.root.size

    '''
     ****     Get items from Treap   ****
    '''

    def _getitem(self, root, index) -> int:
        if (root.left is not None):
            if index <= root.left.size:
                return self._getitem(root.left, index)
            index -= root.left.size
        # root.cnt
        if index in range(1, root.cnt + 1):
            return root.key
        index -= root.cnt
        # definitely to the right
        return self._getitem(root.right, index)

    def __getitem__(self, index):
        if 0 <= index < self.root.size:
            return self._getitem(self.root, index + 1)
        else:
            return None

    def _pivot_up(self, node):
        parent = node.parent
        if parent is None:
            return

        if parent.left == node:

            """
            Given the following binary search tree:

                   GP
                   |
                   P
                  / \
                (N)  P.right
                / \
          N.left   N.right

            Imagine we need to pivot 3 and 5 (to maintain the heap
            property). The resulting tree will look like:

                   GP
                   |
                  (N)
                  / \
            N.Left   P
                    / \
              N.right  P.right

            """

            node.right, parent.left = parent, node.right
            if parent.left:
                parent.left.parent = parent

            node.size += (parent.right.size + parent.cnt) \
                if parent.right else parent.cnt
            parent.size -= (node.left.size + node.cnt) \
                if node.left else node.cnt

        else:

            """
            Given the following binary search tree:

                   GP
                   |
                   P
                  / \
            P.left   N
                    / \
              N.left   N.right

            Imagine we need to pivot 3 and 5 (to maintain the heap
            property). The resulting tree will look like:

                   GP
                   |
                   N
                  / \
                 P  N.right
                / \
          P.left   N.Left

            """

            node.left, parent.right = parent, node.left
            if parent.right:
                parent.right.parent = parent

            node.size += parent.left.size + parent.cnt \
                if parent.left else parent.cnt

            parent.size -= (node.right.size + node.cnt) \
                if node.right else node.cnt

        grandparent = parent.parent
        node.parent, parent.parent = grandparent, node
        if grandparent:
            if grandparent.left == parent:
                grandparent.left = node
            else:
                grandparent.right = node
        else:
            self.root = node

    def _prioritize(self, node):
        while node.parent and node.parent.priority < node.priority:
            self._pivot_up(node)

    def _find_node(self, key, node, parent=None):
        while True:
            if (node is None) or (key == node.key):
                return node, parent
            elif (key < node.key):
                node, parent = node.left, node
            elif (key > node.key):
                node, parent = node.right, node

    def __contains__(self, key):
        node = self._find_node(key, self.root)[0]
        return node is not None

    def insert(self, key):
        # Search Key first
        node, parent = self._find_node(key, self.root)
        if node is None:
            node = TreapNode(key)
            if parent is None:
                self.root = node
            elif node.key <= parent.key:
                parent.left = node
            else:
                parent.right = node

            node.parent = parent
            node.inc_parent_size(node)
            self._prioritize(node)
        else:
            node.cnt += 1
            node.size += 1
            node.inc_parent_size(node)

    def delete(self, key):
        # Search Key first
        node, parent = self._find_node(key, self.root)
        if (node is None):
            # print('Wrong!')
            raise KeyError(key)
        elif node.cnt > 1:
            node.cnt -= 1
            node.size -= 1
            node.decr_parent_size(node)
        elif parent is None and not (node.left and node.right):
            self.root = node.left or node.right
            if (self.root is not None):
                self.root.parent = None
            del node
        else:
            while node.left and node.right:
                # Pivot a child node up while the node to be deleted has
                # both left and right children.
                if node.left.priority > node.right.priority:
                    self._pivot_up(node.left)
                else:
                    self._pivot_up(node.right)

            node.decr_parent_size(node)

            child = node.left or node.right
            if node.parent.left == node:
                node.parent.left = child
                if child:
                    child.parent = node.parent
            else:
                node.parent.right = child
                if child:
                    child.parent = node.parent
            del node

    def _traverse(self, node, attr, parent=None):
        while getattr(node, attr):
            node, parent = getattr(node, attr), node
        return node, parent

    def min(self):
        if self.root is None:
            return None
        node, _ = self._traverse(self.root, 'left')
        return node.key

    def max(self):
        if self.root is None:
            return None
        node, _ = self._traverse(self.root, 'right')
        return node.key

    def median(self) -> float:
        n = self.root.size
        if (n % 2) == 0:
            return (self._getitem(self.root, n // 2 + 1) +
                    self._getitem(self.root, n // 2)) / 2
        else:
            return self._getitem(self.root, math.floor(n / 2) + 1)

    def clear(self):
        self.root = None


if __name__ == '__main__':
    n = int(input())
    T = Treap()
    for _ in range(n):
        T.insert(int(input()))
        print("{:.1f}".format(T.median()))

