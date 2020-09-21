#!/bin/python3


"""
deque Double Ended Queue

Input:
5 4
1 2 3 4 5

Output:
5 1 2 3 4

"""


import math
import os
import random
import re
import sys
from collections import deque

def rotLeft2(a, d):
    d = d%len(a)
    a = a[d:]+a[:d]
    return a

def rotLeft(a, d):
    result = deque(a)
    for i in range(d):
        result.append(result.popleft())
    return result

if __name__ == '__main__':
    

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(' '.join(map(str, result)) + '\n')

