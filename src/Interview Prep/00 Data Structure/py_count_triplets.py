#!/bin/python3

"""
Dictionary
Dict.get()

Input:
4 2
1 2 2 4
Output:
2

Input:
6 3
1 3 9 9 27 81
Output:
6

Input:
5 5
1 5 5 25 125
Output:
4

Input:
100 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
Output:
161700

"""


import math
import os
import random
import re
import sys

from itertools import combinations
def countTriplets1(arr, r):
    result = 0
    for t in combinations(sorted(arr),3):
        if t[1] == t[0]*r and t[2] == t[1]*r:
            result += 1
    return result


def countTriplets(arr, r):
    result = 0
    dict = {}
    dictPairs = {}

    for i in reversed(arr):
        if i*r in dictPairs:
            result += dictPairs[i*r]
        if i*r in dict:
            dictPairs[i] = dictPairs.get(i, 0) + dict[i*r]
        dict[i] = dict.get(i, 0) + 1

    return result

if __name__ == '__main__':


    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(str(ans) + '\n')
