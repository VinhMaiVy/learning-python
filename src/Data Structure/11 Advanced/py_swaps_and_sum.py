#!/bin/python3

"""
Treap with Implicit Keys

Input:
6 4
1 2 3 4 5 6
1 2 5
2 2 3
2 3 4
2 4 5

Output:
5
7
9

"""
# import math
# from random import Random
import os
import sys

from random import random


class Treap:

    def __init__(self, val: int):
        # global R
        # global P
        self.val = val
        # self.priority = R.random()
        self.priority = random()
        # self.priority = P.pop(0)
        self.cnt = 1
        self.summation = val
        # self.parent = None
        self.right = None
        self.left = None

    def swap(self, root, add=1):
        global prev
        counter = root.left.cnt if (root.left is not None) else 0
        counter += add
        if (root.left is not None):
            self.swap(root.left, add)
        if (counter % 2 == 0):
            root.val, prev.val = prev.val, root.val
        else:
            prev = root
        if (root.right is not None):
            self.swap(root.right, counter + 1)

    def upd_sum(self, root):
        if (root.left is None) and (root.right is None):
            root.summation = root.val
            return root.val
        sum_left = (self.upd_sum(root.left) if (root.left is not None) else 0)
        sum_right = (self.upd_sum(root.right) if (root.right is not None) else 0)
        root.summation = root.val + sum_left + sum_right
        return root.summation

    def _getitem(self, root, index) -> int:
        if (root.left is not None):
            if index <= root.left.cnt:
                return self._getitem(root.left, index)
            index -= root.left.cnt
        if index == 1:
            return root.val
        return self._getitem(root.right, index - 1)

    def __getitem__(self, index):
        return self._getitem(self, index)

    def __str__(self):
        res = str(self.left) if (self.left is not None) else ''
        res += str(self.val) + ' '
        res += str(self.right) if (self.right is not None) else ''
        return res

    def __repr__(self):
        lines = []
        nodes = [(self, 0)]
        while nodes:
            node, indent = nodes.pop()
            name = str(node.val) + '-' + str(node.cnt) + '-' + str(node.summation) \
                if (node is not None) else '*'
            lines.append('   ' * indent + name)
            if node is not None:
                nodes.append((node.right, indent + 1))
                nodes.append((node.left, indent + 1))
        return "\n".join(lines)

    def __len__(self):
        return self.cnt

    def sum(self):
        return self.summation


def maxDepth(root: Treap) -> int:
    if (root is None):
        return 0
    leftDepth = maxDepth(root.left)
    rightDepth = maxDepth(root.right)
    if leftDepth > rightDepth:
        return leftDepth + 1
    else:
        return rightDepth + 1


def merge(left: Treap, right: Treap) -> Treap:
    if (left is None) or (right is None):
        return left or right
    if left.priority > right.priority:
        left.cnt += right.cnt
        left.summation += right.summation
        # right.parent = left
        left.right = merge(left.right, right)  # <<<----------- merge
        res = left
    else:
        right.cnt += left.cnt
        right.summation += left.summation
        # left.parent = right
        right.left = merge(left, right.left)  # <<<------------ merge
        res = right
    return res


def split(root: Treap, index: int) -> (Treap, Treap):
    if (root is None):
        return (None, None)
    if (index <= 0):
        return (None, root)
    elif (index >= root.cnt):
        return (root, None)
    if (root.left is not None) and (index <= root.left.cnt):
        resleft, root.left = split(root.left, index)  # <<<---- split
        root.cnt -= resleft.cnt
        root.summation -= resleft.summation
        # resleft.parent = root.parent
        return (resleft, root)
    index -= root.left.cnt if (root.left is not None) else 0
    if (index == 1):  # Found
        resright = root.right
        root.right = None
        root.cnt -= resright.cnt if (resright is not None) else 0
        root.summation -= resright.summation if (resright is not None) else 0
        # resright.parent = root.parent
        return (root, resright)
    root.right, leftover = split(root.right, index - 1)  # <<<- split
    root.cnt -= leftover.cnt
    root.summation -= leftover.summation
    # leftover.parent = root.parent
    return (root, leftover)


def sum_range(root:Treap, a:int, b:int) -> (Treap, int):
    if a == b:
        return (root, root[a])
    if b - a == 1:
        return (root, root[a] + root[b])
    T1, T2 = split(root, a - 1)
    T2, T3 = split(T2, b - a + 1)
    res = T2.summation
    root = merge(T1, T2)
    root = merge(root, T3)
    return (root, res)


def swap_range(root:Treap, a:int, b:int) -> Treap:
    T1, T2 = split(root, a - 1)
    T2, T3 = split(T2, b - a + 1)
    T2.swap(T2)
    T2.upd_sum(T2)
    root = merge(T1, T2)
    root = merge(root, T3)
    return root


if __name__ == '__main__':
    # R = Random()
    # P = [50, 70, 30, 90, 0, 40, 20, 10, 80, 40]
    # n = 5
    # arr = R.sample(range(0, n), n)
    # arr = [4, 5, 2, 3, 0, 1]
    # arr = [2, 2, 2, 2, 2, 2]
    # arr = [1, 2, 3, 4, 5, 6, 7, 8]
    # arr = [1, 2, 3, 4, 5, 6]

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nq = input().split()
    n = int(nq[0])
    q = int(nq[1])
    arr = list(map(int, input().rstrip().split()))
    T = None
    for _ in arr:
        T = merge(T, Treap(_))

    for _ in range(q):
        c, a, b = list(map(int, input().rstrip().split()))
        if c == 1:
            T = swap_range(T, a, b)
            print(T.sum())
        if c == 2:
            T, res = sum_range(T, a, b)
            print(res)
            # fptr.write(str(res) + '\n')

    # fptr.close()
    print()

