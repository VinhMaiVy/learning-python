#!/bin/python3

"""
Standard Deviation

Input:
5
10 40 30 50 20
Output:
14.1

"""

import math

if __name__ == '__main__':
    
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    
    mean = sum(a)/n
    
    stddev = math.sqrt(sum([(n-mean)**2 for n in a])/n)
    
    print("{:.1f}".format( stddev ))
