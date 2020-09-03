#!/bin/python3

"""
BubbleSort

Input
6
1 2 3 4 5 3

7
7 1 3 2 4 5 6

"""

import math
import os
import random
import re
import sys


# Complete the countSwaps function below.
def countSwaps(a):
    len_a= len(a)
    swapCount = 0
    for i in range(len_a):
        for j in range(len_a-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapCount += 1
    print('Array is sorted in ' + str(swapCount) + ' swaps.')    
    print('First Element:', a[0])
    print('Last Element:',  a[len_a-1])
    
if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
