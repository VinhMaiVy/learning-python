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
        # self.priority = R.random()
        # self.priority = random()
        self.priority = val
        self.cnt = 1
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
                self._setitem(root.left, index, val)
            index -= root.left.cnt
        if index == 1:  # Found!
            root.val = val
        elif index > 1:  # definitely to the right
            self._setitem(root.right, index - 1, val)

    def __setitem__(self, index, val: int):
        if 0 <= index < self.cnt:
            self._setitem(self, index + 1, val)

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
            name = 'p:' + str(node.priority) + '-c:' + str(node.cnt) + '-v:' + str(node.val) \
                if (node is not None) else '*'
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

    if left.priority < right.priority:
        left.cnt += right.cnt  # <<<-------------------------- cnt
        left.right = merge(left.right, right)
        res = left
    else:
        right.cnt += left.cnt  # <<<-------------------------- cnt
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
        return resleft, root
    elif index > cur_ind:
        root.right, resright = split(root.right, index, cur_ind + 1)
        root.cnt -= resright.cnt if (resright is not None) else 0
        return root, resright

    else:
        resleft = root.left
        root.left = None
        root.cnt -= resleft.cnt if (resleft is not None) else 0
        # upd_minimum(resleft)
        # upd_minimum(root)
        return resleft, root


def insertAt(root: Treap, index: int, val: int) -> Treap:
    if root is None:
        return Treap(val)
    else:
        left, right = split(root, index)
        left = merge(left, Treap(val))
        root = merge(left, right)
        return root


def eraseAt(root: Treap, index: int) -> Treap:
    left, right = split(root, index)
    _t, right = split(right, 1)
    del _t
    return merge(left, right)


def append(root: Treap, val: int) -> Treap:
    return merge(root, Treap(val))


def appendleft(root: Treap, val: int) -> Treap:
    return merge(Treap(val), root)


def pop(root: Treap) -> (Treap, int):
    _last = len(root) - 1
    val = root[_last]
    left, right = split(root, _last)
    _t, right = split(right, 1)
    del _t
    return (merge(left, right), val)


def popleft(root: Treap) -> (Treap, int):
    val = root[0]
    left, right = split(root, 0)
    _t, right = split(right, 1)
    del _t
    return (merge(left, right), val)


def poproot(root: Treap) -> (Treap, int):
    _val = root.val
    left, right = root.left, root.right
    del root
    return (merge(left, right), _val)


if __name__ == '__main__':
    R = Random()
    n = 8

    arr = R.sample(range(0, n), n)
    # arr = [4, 2, 1, 6, 3, 0, 5]
    # arr = [1, 2, 3, 4, 5, 6, 7]

    t = None
    for a in arr:
        t = merge(t, Treap(a))
    print(t)
    print(repr(t))
    t.sort()

