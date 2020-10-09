#!/bin/python3

"""
Treap with Implicit Keys

"""
# import math
from random import Random
# from random import random


class Treap:

    def __init__(self, val: int):
        global R
        self.val = val
        self.priority = R.random()
        # self.priority = random()
        self.cnt = 1
        self.summation = val
        self.right = None
        self.left = None

    def _getitem(self, root, index) -> int:
        if (root.left is not None):
            if index <= root.left.cnt:
                return self._getitem(root.left, index)
            index -= root.left.cnt
        if index == 1:
            return root.val
        return self._getitem(root.right, index - 1)

    def __getitem__(self, index):
        # if 1 <= index <= self.cnt:
        return self._getitem(self, index)
        # else:
        #    return None

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
            name = str(node.val) if (node is not None) else '*'
            lines.append('   ' * indent + name)
            if node is not None:
                nodes.append((node.right, indent + 1))
                nodes.append((node.left, indent + 1))
        return "\n".join(lines)

    def __len__(self):
        return self.cnt


def merge(left: Treap, right: Treap) -> Treap:
    if (left is None) or (right is None):
        return left or right

    if left.priority > right.priority:
        left.cnt += right.cnt  # <<<-------------------------- cnt
        left.summation += right.summation
        left.right = merge(left.right, right)
        res = left
    else:
        right.cnt += left.cnt  # <<<-------------------------- cnt
        right.summation += left.summation
        right.left = merge(left, right.left)
        res = right
    return res


def split(root: Treap, index: int, add=0) -> (Treap, Treap):
    if (root is None):
        return (None, None)

    if (index <= 0):
        return (None, root)

    cur_ind = root.left.cnt if (root.left is not None) else 0
    cur_ind += add

    if index < cur_ind:
        resleft, root.left = split(root.left, index, add)
        root.cnt -= resleft.cnt if (resleft is not None) else 0
        root.summation -= resleft.summation if (resleft is not None) else 0
        return resleft, root
    elif index > cur_ind:
        root.right, resright = split(root.right, index, cur_ind + 1)
        root.cnt -= resright.cnt if (resright is not None) else 0
        root.summation -= resright.summation if (resright is not None) else 0
        return root, resright
    else:
        resleft = root.left
        root.left = None
        root.cnt -= resleft.cnt if (resleft is not None) else 0
        root.summation -= resleft.summation if (resleft is not None) else 0
        return resleft, root


def sum_range(root:Treap, a:int, b:int) -> (Treap, int):
    if a == b:
        return (root, root[a])
    if b - a == 1:
        return (root, root[a] + root[b])
    T1, T2 = split(root, a)
    T2, T3 = split(T2, b - a + 1)
    res = T2.summation
    root = merge(T1, T2)
    root = merge(root, T3)
    return (root, res)


if __name__ == '__main__':
    R = Random(3)
    # n = 50
    # arr = R.sample(range(0, n), n)
    # arr = [4, 5, 2, 3, 0, 1]
    arr = [1, 1, 1, 1, 1]
    arr2 = [2, 2, 2, 2, 2]

    t = None
    for a in arr:
        t = merge(t, Treap(a))
    print(t)
    print(t.summation)

    t2 = None
    for a in arr2:
        t2 = merge(t2, Treap(a))
    print(t2)
    print(t2.summation)

    t = merge(t, t2)
    print(t)
    print(t.summation)

    l, r = split(t, 3)
    print(l)
    print(l.summation)

    print(r)
    print(l.summation)

    t = merge(l, r)
    print(t)
    print(l.summation)

