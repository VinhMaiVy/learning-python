#!/bin/python3

"""
Arrays

Input:
-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0 
Output:
28

Input:
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Output:
19

"""


import math
import os
import random
import re
import sys


def hourglassSum(arr):
    result = float('-inf')
    for i in range(4):
        for j in range(4):
            s = sum(arr[j][i:i+3]) + arr[j+1][i+1] + sum(arr[j+2][i:i+3])            
            if s > result:
                result = s                        
    return(result)

if __name__ == '__main__':
    
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(str(result) + '\n')

    
