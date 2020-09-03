#!/bin/python3

"""
Counter
Set

Input:
2
hello
world
hi
world

Output:
YES
NO

"""


import math
import os
import random
import re
import sys
from collections import Counter

def twoStrings(s1, s2):
    return "YES" if set(s1) & set(s2) else "NO"

def twoStrings2(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    return 'NO' if (c1 - c2) == c1 else 'YES'

if __name__ == '__main__':
    
    q = int(input())

    for q_itr in range(q):
        s1 = input()
        s2 = input()

        result = twoStrings(s1, s2)

        print(result + '\n')
