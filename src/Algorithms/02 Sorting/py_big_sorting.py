#!/bin/python3

"""
Python

Input:
6
31415926535897932384626433832795
1
3
10
3
5

Output:
1
3
3
5
10
31415926535897932384626433832795

"""


import math
import os
import random
import re
import sys
from functools import cmp_to_key

def big_cmp(x, y):
    i = len(x)
    j = len(y)
    if(i==j):
        if x == y:
            return 0
        else:
            return 1 if x>y else -1
    else:    
        return i-j   

def bigSorting(unsorted):
    unsorted.sort(key=cmp_to_key(big_cmp))
    for s in unsorted:
        yield(s)

if __name__ == '__main__':

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    print('\n'.join(result))
   
