#!/bin/python3

"""
Python

Input:
2
.*\+
.*+

Output:
True
False

"""

import re

if __name__ == '__main__':    
    n = int(input())
    for _ in range(n):
        try:            
            re_pattern = re.compile(input())
        except:
            print('False')            
        else:
            print('True')
