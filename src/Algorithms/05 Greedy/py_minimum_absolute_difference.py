#!/bin/python3

"""
Counter

Input:
10
-59 -36 -13 1 -53 -92 -2 -96 -54 75

Output:
1

"""


import math
import os
import random
import re
import sys
from collections import Counter

def minimumAbsoluteDifference(arr):
    s_arr = sorted(arr)
    result = float('inf')    
    current = s_arr[0]
    for i in range(1,len(s_arr)):
        diff = abs(current - s_arr[i])        
        if  diff < result:
            result = diff
        current = s_arr[i]     
    return result

if __name__ == '__main__':
    
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(str(result) + '\n')
