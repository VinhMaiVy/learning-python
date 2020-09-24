#!/bin/python3

"""
reduce lambda

Input:
6 3
1 3 2 6 1 2

Output:
5

Input:

100 96
34 38 30 27 1 81 37 19 74 73 32 13 44 99 7 88 50 52 32 82 29 1 55 85 89 58 35 19 76 55 45 37 41 74 80 46 38 74 56 18 86 23 57 27 52 9 69 78 52 8 62 85 65 2 11 70 34 26 72 11 20 32 9 75 74 85 29 6 87 81 40 11 31 49 66 91 99 85 18 54 81 93 52 9 72 89 85 66 24 11 85 3 14 36 72 3 76 99 88 8

Output:
65


"""


import math
import os
import random
import re
import sys

from itertools import combinations
from functools import reduce
from collections import Counter

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):     
    return Counter(map(lambda x:(x[0]+x[1])%k, list(combinations(ar,2))))[0] 
    
if __name__ == '__main__':


    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(str(result) + '\n')


