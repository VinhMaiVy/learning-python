#!/bin/python3
"""
Python

Input:
4

Output:
6

"""

import math
import os
import random
import re
import sys


# Complete the strangeCounter function below.
def strangeCounter(t):
    k = math.log2(t / 3 + 1) - 1
    kc = math.ceil(k)
    s = 3 * (2 ** (kc + 1) - 1)
    return s - t + 1


if __name__ == '__main__':
    t = int(input())
    result = strangeCounter(t)
    print(str(result) + '\n')
