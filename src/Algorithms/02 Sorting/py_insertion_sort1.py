#!/bin/python3

import math
import os
import random
import re
import sys

"""
Python

Input:
5
2 4 9 8 1

Output:
2 4 6 8 8 
2 4 6 6 8 
2 4 4 6 8 
2 3 4 6 8

Input:
5
1 2 4 5 3

Output:
1 2 4 5 5
1 2 4 4 5
1 2 3 4 5


"""


# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    n -= 1
    stored = arr[n]
    while n >= 0:
        if (n == 0) or (arr[n - 1] < stored):
            arr[n] = stored
            print(" ".join(map(str, arr)))
            break
        else:
            arr[n] = arr[n - 1]
            print(" ".join(map(str, arr)))
        n -= 1


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
