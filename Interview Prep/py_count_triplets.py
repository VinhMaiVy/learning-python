#!/bin/python3

"""
Python

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


from collections import OrderedDict
def countTriplets(arr, r):
    result = 0

    arr_dict = OrderedDict()
    for i in arr:
        li = math.log(i,r)
        if li.is_integer():
            li = int(li)
            if li in arr_dict:
                arr_dict[li] += 1
            else:
                arr_dict[li] = 1
                
    print(arr_dict)
                    
    return result


if __name__ == '__main__':


    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(str(ans) + '\n')
