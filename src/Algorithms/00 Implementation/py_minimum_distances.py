#!/bin/python3

"""
Dictionary

Input:
6
7 1 3 4 1 7

Output:
3

"""


import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    d = {}
    result = float('inf')
    for i in range(len(a)):
        d[a[i]] =  d.get(a[i],[]) + [i]
        
    for k in d.keys():
        if len(d[k]) == 2:
            result = min(result, abs(d[k][0] - d[k][1]))
        
    return result if result < float('inf') else -1 


if __name__ == '__main__':
    
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    print(str(result) + '\n')
