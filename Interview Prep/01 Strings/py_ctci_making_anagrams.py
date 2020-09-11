#!/bin/python3

"""
Counter

Input:
cde
abc

Output:
4

"""


import math
import os
import random
import re
import sys
from collections import Counter

def makeAnagram(a, b):
    ca = Counter(a)
    cb = Counter(b)    
    return sum((ca-cb).values()) + sum((cb-ca).values()) 

if __name__ == '__main__':
    
    a = input()
    b = input()

    res = makeAnagram(a, b)

    print(str(res) + '\n')
