#!/bin/python3

"""
Counting on string

Input:
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB

Output:
3
4
0
0
4

"""


import math
import os
import random
import re
import sys


def alternatingCharacters(s):
    result = 0
    pos = 0
    c = s[0]    
    while pos+1 < len(s):
        pos += 1
        if s[pos] == c:
            result += 1
        else:
            c = s[pos]
    return result
    

if __name__ == '__main__':
    
    q = int(input())

    for q_itr in range(q):
        s = input()
        result = alternatingCharacters(s)
        print(str(result) + '\n')    
