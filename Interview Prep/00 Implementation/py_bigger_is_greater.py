#!/bin/python3

"""
String Indexing

Input:
5
ab
bb
hefg
dhck
dkhc

Output:
ba
no answer
hegf
dhkc
hcdk

"""


import math
import os
import random
import re
import sys


def biggerIsGreater(w):
    result = ''    
    index = len(w)-1
    while index:
        if w[index-1] < w[index]:
            for c in sorted(w[index:]):
                if c > w[index-1]:
                    break
            i = w.find(c,index)
            wl = list(w)
            wl[index-1], wl[i] = wl[i], wl[index-1]
            w = "".join(wl)
            result = w[:index] + "".join(sorted(w[index:]))
            break 
        index -= 1
             
    if result:
        return result
    else:
        return 'no answer' 

if __name__ == '__main__':
    
    T = int(input())

    for T_itr in range(T):
        w = input()
        result = biggerIsGreater(w)
        print(result + '\n')       
