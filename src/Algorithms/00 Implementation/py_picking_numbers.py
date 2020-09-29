#!/bin/python3

"""
Python

Input:
6
4 6 5 3 3 1

Output:
3

Input:
9
1 1 2 2 4 4 5 5 5

Output:
5


"""


import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a.sort()
    result = 1
    counter = 1
    min = a[0]
    for current in a[1:]:
        if abs(current - min) <= 1:
            counter += 1
        else:
            if counter > result:
                result = counter
            counter = 1
            min = current
        if counter > result:
            result = counter
        previous = current
    return result

if __name__ == '__main__':
    
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(str(result) + '\n')
