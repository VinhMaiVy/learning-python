#!/bin/python3

"""
Python

Input:
8 4
1 2 3 4 5 6 7 8
1 2 4
2 3 5
1 4 7
2 1 4

Output:
1
2 3 6 5 7 8 4 1

"""

import math
import os
import random
import re
import sys


def QueryArray(n, arr, queries):

    tmp = [0] * n

    # print(" ".join(map(str,arr)))
    for q in queries:
        t, i, j = q
        i, j = i - 1, j - 1
        if t == 1:
            tmp[0:i] = arr[0:i]
            arr[0:j - i + 1] = arr[i:j + 1]
            arr[j - i + 1:j + 1] = tmp[0:i]
        elif t == 2:
            tmp[j + 1:n] = arr[j + 1:n]
            arr[n - 1 - j + i:n] = arr[i:j + 1]
            arr[i:n - j + i - 1] = tmp[j + 1:n]
        # print(" ".join(map(str,arr)))

    print(abs(arr[0] - arr[n - 1]))
    print(" ".join(map(str, arr)))


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    arr = list(map(int, input().split()))

    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().split())))

    result = QueryArray(n, arr, queries)

