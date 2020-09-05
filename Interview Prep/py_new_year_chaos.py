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


def minimumBribes(q):
    result = 0
    len_a = len(arr)    
    for n in range(1,len_a+1):            
        if (arr[n] == n):
            continue
        else:
            c = arr[n]
            max = 0
            while (c != n):                
                c = c+1 if c>n else c-1 
                result +=1
                max += 1
            if max > 2:
                return 'Too Chaotic'
    return result

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))
        print(q)
        
        minimumBribes(q)
