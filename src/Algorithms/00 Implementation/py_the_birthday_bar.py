#!/bin/python3

"""
Python

Input:
5
1 2 1 3 2
3 2

Output:
2

"""


import math
import os
import random
import re
import sys

def birthday(s, d, m):
    tp = (len(s)-m) + 1
    return len([1 for i in range(tp) if sum(s[i:i+m])==d])

if __name__ == '__main__':
    
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(str(result) + '\n')
