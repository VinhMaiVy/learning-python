#!/bin/python3

"""
Python

Input:
5  
1 1 2 4 2

Output:
8

"""


import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(arr):
    result = 0
    d = {}
    for i in range(len(arr)):
        a = arr[i]
        d[a] = d.get(a,[]) + [i]
    return d

if __name__ == '__main__':
    
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)
    
    print(result)
    #print(str(result) + '\n')
    
