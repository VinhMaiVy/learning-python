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
    len_q = len(q)
    dic_q = dict()    
    
    for n in range(len_q):
        dic_q[q[n]] = n
                
    for n in range(len_q):
        if q[n]-1>0:
            if dic_q[q[n]-1] > n:
                result +=1
        if q[n]-2>0:
            if dic_q[q[n]-2] > n:
                result +=1
        if q[n]-3>0:
            if dic_q[q[n]-3] > n:
                result = 0
                break    
    if result:
        print(result)
    else:
        print('Too chaotic')
                            
    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))
        #print(q)        
        minimumBribes(q)
