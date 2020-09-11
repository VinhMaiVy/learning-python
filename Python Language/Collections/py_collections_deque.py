#!/bin/python3

"""
Double Ended Queue

https://docs.python.org/3/library/collections.html#collections.deque


deque
getattr

Input:
6
append 1
append 2
append 3
appendleft 4
pop
popleft

Output:
1 2

"""

from collections import deque

if __name__ == '__main__':
    d = deque()
    n = int(input())
    for _ in range(n):
        cmd, *args = input().split()
        getattr(d, cmd)(*args)
    print(*[e for e in d])
