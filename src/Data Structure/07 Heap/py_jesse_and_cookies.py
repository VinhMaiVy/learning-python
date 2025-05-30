#!/bin/python3

"""
Python
    Priority-Queue
    Binary Heap Tree

Input:
6 12
1 2 3 9 10 15

Output:
3

Input:
10 7
5 3 2 1 6 7 8 9 10 4

10 7
10 9 8 7 6 5 4 3 2 1

"""


import os
import sys
import math

class BinaryHeapTree(object):

    def __init__(self, max_nodes=1000000):
        self._max_nodes = max_nodes
        self.heap = [0]*(self._max_nodes+1)
        self._n = 0

    def __str__(self):
        return str(self.heap[1:self._n+1])

    def isRoot(self, i):
        return i == 1

    def level(self, i):  # return the level of a node
        return int(math.log(i, 2))

    def parent(self, i):  # return the parent of a node
        return i // 2

    def left(self, i):  # return the left node of a node
        return 2 * i

    def right(self, i):  # return the right node of a node
        return 2 * i + 1

    def len(self):
        return self._n

    def min(self):
        return self.heap[1]

    def heapEmpty(self):
        return self._n == 0

    def bubbleUp(self, i):
        if self.isRoot(i):
            return
        else:
            _parent = self.parent(i)
            if self.heap[i] < self.heap[_parent]:
                self.heap[i], self.heap[_parent] = self.heap[_parent], self.heap[i] 

            self.bubbleUp(self.parent(i))

    def bubbleDown(self, i):
        if self.left(i) > self._n:
            return  # no children
        elif self.right(i) > self._n:  # only left child
            _left = self.left(i)
            if self.heap[i] > self.heap[_left]:
                self.heap[i], self.heap[_left] = self.heap[_left], self.heap[i]
        else:  # two children
            _left = self.left(i)
            _right = self.right(i)
            if self.heap[_left] < self.heap[_right] and self.heap[i] > self.heap[_left]:
                self.heap[i], self.heap[_left] = self.heap[_left], self.heap[i]
                self.bubbleDown(_left)
            elif self.heap[i] > self.heap[_right]:
                self.heap[i], self.heap[_right] = self.heap[_right], self.heap[i]
                self.bubbleDown(_right)

    def insert(self, p):
        self._n += 1
        self.heap[self._n] = p
        self.bubbleUp(self._n)

    def pop(self):
        _p = self.heap[1]
        self.heap[1] = self.heap[self._n]
        # self.heap[self._n] = 0
        self._n -= 1
        self.bubbleDown(1)
        return _p

    def delete(self, i):
        self.heap[i] = self.heap[self._n]
        # self.heap[self._n] = 0
        self._n -= 1
        self.bubbleUp(i)
        self.bubbleDown(i)

    def root(self):
        if self.heapEmpty(self):
            return None
        else:
            return self.heap[1]

    def heapify(self, arr):
        self._n = len(arr)
        self.heap[1:] = arr
        for i in range(self._n//2, 0, -1):
            self.bubbleDown(i)


def cookies(k, A):
    result = 0
    heap = BinaryHeapTree(len(A))
    heap.heapify(A)    
    
    while heap.len()>=2 and heap.min() <= k:
        heap.insert(heap.pop() + 2*heap.pop())
        result += 1    
    
    if heap.min() >= k:
        return result
    else:
        return -1

from collections import deque

def combine(a, b):
    return a + b * 2

def cookies2(k, A):
    result = 0
    queue = deque(sorted(A))
    new_queue = deque()
    top_two = []
    
    while queue:
        if queue and new_queue and len(queue) == 1:
            while new_queue:
                #print('adding new at the end:', new_queue[0])
                queue.append(new_queue.popleft())

        if queue and new_queue and new_queue[0] <= queue[0]:
            #print('adding to queue:', new_queue[0])
            queue.appendleft(new_queue.popleft())

        if queue and len(top_two) == 0 and k <= queue[0]:
            break

        cookie = queue.popleft()
        #print('cookie:', cookie)
        top_two.append(cookie)

        if len(top_two) == 2:
            #print('combine:', top_two[0], top_two[1])
            new_cookie = combine(top_two[0], top_two[1])
            #print('new cookie:', new_cookie)
            top_two = []
            new_queue.append(new_cookie)
            result += 1
    
    while new_queue:
        queue.append(new_queue.popleft())
    
    #print('final:', queue)
    if any(x < k for x in queue):
        return -1
    else:
        return result    

if __name__ == '__main__':
    
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    A = list(map(int, input().rstrip().split()))

    result = cookies2(k, A)
    print(str(result))
