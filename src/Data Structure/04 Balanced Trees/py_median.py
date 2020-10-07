#!/bin/python

"""
Balanced Tree

Input:
7
r 1  
a 1  
a 2  
a 1  
r 1  
r 2  
r 1
r 1

Output:
Wrong!  
1  
1.5  
1  
1.5  
1  
Wrong!

"""
import math
from random import Random
# from random import random


class TreapNode:

    def __init__(self, key, parent=None, left=None, right=None):
        global R
        self.key = key
        self.priority = R.random()
        self.cnt = 1
        self.size = 1
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return str((self.key, int(self.priority * 100), self.size))

    def __str__(self):
        return str((self.key, self.size))
        # return str(self.size)

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
        """Return a string representation of treap."""
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
        return self._str(self.root) if (self.root is not None) else ""

    def __len__(self):
        return self.root.size

    def _getitem(self, root, index) -> int:
        if (root.left is not None):
            if index <= root.left.size:
                return self._getitem(root.left, index)
            index -= root.left.size

        # root.cnt
        if index in [1 + _ for _ in range(root.cnt)]:
            return root.key

        # definitely to the right
        return self._getitem(root.right, index - 1)

    def __getitem__(self, index):
        return self._getitem(self.root, index + 1)

    def _pivot_up(self, node):
        parent = node.parent
        if parent is None:
            return

        if parent.left == node:
            """
            Given the following binary search tree:
                   P
                  / \
                (N)  P.right
                / \
          N.left   N.right

            Imagine we need to pivot 3 and 5 (to maintain the heap
            property). The resulting tree will look like:

                  (N)
                  / \
            N.Left   P
                    / \
              N.right  P.right

            """
            node.right, parent.left = parent, node.right
            if parent.left:  # node.right -> P.left
                parent.left.parent = parent

            if (parent.right is not None):
                node.size += (parent.right.size + parent.cnt)
            else:
                node.size += parent.cnt

            if (node.left is not None):
                parent.size -= (node.left.size + node.cnt)
            else:
                parent.size -= node.cnt

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

            if (parent.left is not None):
                node.size += parent.left.size + parent.cnt
            else:
                node.size += parent.cnt

            if (node.right is not None):
                parent.size -= (node.right.size + node.cnt)
            else:
                parent.size -= node.cnt

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
        while node.parent and (node.parent.priority < node.priority):
            self._pivot_up(node)

    def _find_node(self, key, node, parent=None):
        while True:
            if (node is None) or (key == node.key):
                return node, parent
            elif (key < node.key):
                node, parent = node.left, node
            elif (key > node.key):
                node, parent = node.right, node

    def insert(self, key):
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

    def __contains__(self, key):
        node = self._find_node(key, self.root)[0]
        return node is not None

    def delete(self, key):
        node, parent = self._find_node(key, self.root)
        if (node is None):
            print('Wrong!')
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

    def clear(self):
        self.root = None

    def _traverse(self, node, attr, parent=None):
        while getattr(node, attr):
            node, parent = getattr(node, attr), node
        return node, parent


def median(t) -> float:
        n = len(t)
        if (n % 2) == 0:
            return (t[n // 2] + t[n // 2 - 1]) / 2
        else:
            m = math.floor(n / 2)
            if n > 10:
                print('Accessing:', m - 1, t[m - 1])
                print('Accessing:', m + 1, t[m + 1])
            return t[m]


if __name__ == '__main__':
    R = Random(0)
    N = int(input())
    T = Treap()
    for i in range(0, N):
        tmp = input().strip().split(' ')
        c, k = [ck for ck in tmp]
        k = int(k)
        if c == 'a':
            T.insert(k)
            x = median(T)
            print('T:', T.root.size, "M: {1:0.{0}f}".format(int(not float(x).is_integer()), x))
        elif c == 'r':
            if T.root is None:
                print('Wrong!')
            else:
                if k in T:
                    T.delete(k)
                    if T.root is not None:
                        x = median(T)
                        print('T:', T.root.size , "M: {1:0.{0}f}".format(int(not float(x).is_integer()), x))
                    else:
                        print('Wrong!')
                else:
                    print('Wrong!')

