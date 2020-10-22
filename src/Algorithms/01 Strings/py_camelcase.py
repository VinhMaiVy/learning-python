#!/bin/python3

"""
Python

Input:
saveChangesInTheEditor

Output:
5

"""

import math
import os
import random
import re
import sys


# Complete the camelcase function below.
def camelcase(s):
    res = 1
    for c in s:
        res += 1 if c.isupper() else 0
    return res


if __name__ == '__main__':

    s = input()

    result = camelcase(s)

    print(str(result) + '\n')
