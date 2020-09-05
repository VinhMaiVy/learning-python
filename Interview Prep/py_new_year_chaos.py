#!/bin/python3

"""
Python

Input:
2
5
2 1 5 3 4
5
2 5 1 3 4

Output:
3
Too chaotic

"""


import math
import os
import random
import re
import sys
from collections import Counter

def minimumBribes(q):
    result = 0    
    q = set(q)
    len_q = len(q)
        
    for n in range(len_q):
        max = 0            
        for m in range(n,len_q):
            if q[n] > q[m]:
                result += 1
                max += 1
                if max > 2:                    
                    break
        if max > 2:
            break   
    if max > 2:        
        print('Too chaotic')
    else:
        print(result)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))
        #print(q)        
        minimumBribes(q)
