#!/bin/python3

"""
Python

Input:
10
203 204 205 206 207 208 203 204 205 206
13
203 204 204 205 206 207 205 208 203 206 205 206 204

Output:
204 205 206

"""

import math
import os
import random
import re
import sys

from collections import Counter


def missingNumbers(arr, brr):
    carr = Counter(arr)
    cbrr = Counter(brr)
    res = cbrr - carr
    return list(sorted(res.keys()))


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    print(' '.join(map(str, result)))
    print('\n')

