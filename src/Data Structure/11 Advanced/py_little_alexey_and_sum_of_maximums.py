#!/bin/python3

"""
Treap Split Merge

Input:
3 6
1 3 2
1 1
1 2
1 3
2 2
2 3
3 3

Output:
1
7
15
3
8
2

"""

"""
Treap with Implicit Keys

"""
import os
import sys
from random import random
from itertools import combinations_with_replacement


class Treap:

    def __init__(self, val: int):
        # global R
        self.val = val
        # self.priority = R.random()
        self.priority = random()
        self.cnt = 1
        self.maximum = val
        self.right = None
        self.left = None

    def _getitem(self, root, index) -> int:
        if (root.left is not None):
            if index <= root.left.cnt:
                return self._getitem(root.left, index)
            index -= root.left.cnt
        if index == 1:  # Found!
            return root.val
        # definitely to the right
        return self._getitem(root.right, index - 1)

    def __getitem__(self, index):
        if 0 <= index < self.cnt:
            return self._getitem(self, index + 1)
        else:
            return None

    def _setitem1(self, root, index: int, val: int):
        if (root.left is not None):
            if index <= root.left.cnt:
                self._setitem1(root.left, index, val)
            index -= root.left.cnt
        if index == 1:  # Found!
            root.val = val
        elif index > 1:  # definitely to the right
            self._setitem1(root.right, index - 1, val)

    def _setitem2(self, root, index: int, val: int, add=0):
        cur_ind = root.left.cnt if (root.left is not None) else 0
        cur_ind += add
        if (index < cur_ind):
            self._setitem2(root.left, index, val, add)
        elif (index > cur_ind):
            self._setitem2(root.right, index, val, cur_ind + 1)
        else:
            root.val = val

    def __setitem__(self, index, val: int):
        if 0 <= index < self.cnt:
            self._setitem1(self, index + 1, val)

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
            name = 'p:' + str(node.priority * 100)[0:2] + '-c:' + str(node.cnt) + '-v:' + str(node.val) \
                if (node is not None) else '*'
            lines.append('   ' * indent + name)
            if node is not None:
                nodes.append((node.right, indent + 1))
                nodes.append((node.left, indent + 1))
        return "\n".join(lines)

    def __len__(self):
        return self.cnt


def maxDepth(root: Treap) -> int:
    if (root is None):
        return 0
    leftDepth = maxDepth(root.left)
    rightDepth = maxDepth(root.right)
    if leftDepth > rightDepth:
        return leftDepth + 1
    else:
        return rightDepth + 1


def maximum(root: Treap) -> int:
    if (root is not None):
        return root.maximum
    else:
        return float('-inf')


def upd_maximum(root: Treap):
    if (root is not None):
        root.maximum = max(root.val, max(maximum(root.left),
                                         maximum(root.right)))


def merge(left: Treap, right: Treap) -> Treap:
    if (left is None) or (right is None):
        return left or right

    if left.priority > right.priority:
        left.cnt += right.cnt  # <<<-------------------------- cnt
        left.right = merge(left.right, right)
        res = left
    else:
        right.cnt += left.cnt  # <<<-------------------------- cnt
        right.left = merge(left, right.left)
        res = right

    upd_maximum(res)
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
        upd_maximum(resleft)
        upd_maximum(root)
        return resleft, root
    elif index > cur_ind:
        root.right, resright = split(root.right, index, cur_ind + 1)
        root.cnt -= resright.cnt if (resright is not None) else 0
        upd_maximum(resright)
        upd_maximum(root)
        return root, resright
    else:
        resleft = root.left
        root.left = None
        root.cnt -= resleft.cnt if (resleft is not None) else 0
        upd_maximum(resleft)
        upd_maximum(root)
        return resleft, root


def maximum_range(root:Treap, a:int, b:int) -> (Treap, int):
    if a == b:
        return (root, root[a - 1])
    if abs(b - a) == 1:
        return (root, max(root[a - 1], root[b - 1]))
    T1, T2 = split(root, a - 1)
    T2, T3 = split(T2, b - a + 1)
    res = maximum(T2)
    root = merge(T1, T2)
    root = merge(root, T3)
    return (root, res)


def solve(a, queries):
    T = None
    for _ in a:
        T = merge(T, Treap(_))
    for a, b in queries:
        if a == b:
            res = T[a - 1]
        else:
            res = 0
            for aa, bb in list(combinations_with_replacement(list(range(a, b + 1)), 2)):
                T, r = maximum_range(T, aa, bb)
                res += r
        yield res


if __name__ == '__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    a = list(map(int, input().rstrip().split()))

    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(a, queries)
    print('\n'.join(map(str, result)))
    print('\n')

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()

