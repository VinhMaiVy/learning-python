#!/bin/python3

"""
Python

Input:
8 4
1 2 3 4 5 6 7 8
1 2 4
2 3 5
1 4 7
2 1 4

Output:
1
2 3 6 5 7 8 4 1

"""

import math
import os
import random
import re
import sys
from random import random

class Treap:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.size = 1
        self.right = None
        self.left = None

    def __getitem__(self, index):
        if self.left and index <= self.left.size:
            return self.left[index]

        index -= self.left.size if self.left else 0

        if index == 1:
            return self.data

        return self.right[index - 1]

    def __str__(self):
        res = str(self.left) if self.left else ''
        res += str(self.data) + ' '
        res += str(self.right) if self.right else ''
        return res

    def merge(self, left, right):  # print('merging')
        if not (left and right):
            return left or right

        if left.priority > right.priority:
            left.size += right.size
            left.right = self.merge(left.right, right)
            # print('returning left:', left.data)
            return left

        # left is smaller
        right.size += left.size
        right.left = self.merge(left, right.left)
        # print('returning right:', right.data)
        return right

    def split(self, index):
        if not index:
            return None, self
        if not self:
            return None, None

        # print('asked to split', t.data, t.size, 'on', index)

        if index == self.size:
            # print('index == t.size, returning', t.data)
            return self, None

        if self.left and self.left.size >= index:
            # print('t.l.s:', t.left.size, '>=', index)
            res, self.left = self.left.split(index)
            self.size -= res.size
            return res, self

        index -= self.left.size if self.left else 0
        # rint('index is now', index)
        if index == 1:
            # print('index is 1, cut off', t.right.data
            # if t.right else 'None', 'and return', t.data)
            temp = self.right
            self.right = None
            self.size -= temp.size
            return self, temp

        # definitely to the right
        self.right, leftover = self.right.split(index - 1)
        # print('taking leftovers')
        self.size -= leftover.size
        # leftover exists because we already checked
        # if they wanted everyhing at the top
        return self, leftover

def handle(treap, c, i, j):
    left, treap.root = treap.split(i)
    # print('left: ', left)
    treap.root, right = treap.split(j - i)
    # print('right: ', right)
    result = treap.merge(left, right)
    # print('merge: ', result)
    # print('cut: ', treap.root)

    if c == 1:
        result = treap.merge(treap.root, result)
    elif c == 2:
        result = treap.merge(result, treap.root)

    # print('result: ', result, '\n')
    return result

def QueryArray(n, arr, queries):    
    treap = Treap(arr[0], random())
    for i in arr[1:]:
        treap = treap.merge(treap, Treap(i, random()))
    #print(treap)
    
    for c, i, j in queries:
        treap = handle(treap, c, i-1, j)
    
    print(abs(treap[1] - treap[n]))
    print(treap)

def QueryArray2(n, arr, queries):    

    tmp = [0]*n
            
    #print(" ".join(map(str,arr)))            
    for q in queries:
        t, i, j = q
        i, j = i-1, j-1
        if t == 1:
            tmp[0:i] = arr[0:i]
            arr[0:j-i+1] = arr[i:j+1]
            arr[j-i+1:j+1] = tmp[0:i]  
        elif t == 2:
            tmp[j+1:n] = arr[j+1:n]
            arr[n-1-j+i:n] = arr[i:j+1]
            arr[i:n-j+i-1] = tmp[j+1:n]
        #print(" ".join(map(str,arr)))
        
    print(abs(arr[0]-arr[n-1]))
    print(" ".join(map(str,arr)))

    
if __name__ == '__main__':
    
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    arr = list(map(int, input().split())) 

    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().split())))

    result = QueryArray(n, arr, queries)
    
    
