#!/bin/python3

"""
Poisson Distribution 1
https://www.hackerrank.com/challenges/s10-poisson-distribution-1/tutorial

Input:
0.88 1.55

Output:
226.176
286.100

"""

import math

def poisson_distribution(k,l):
    return (l**k)*math.exp(-l)/math.factorial(k)

if __name__ == '__main__':
    
    la, lb = list(map(float, input().rstrip().split()))
    
    # print(la, lb)   
    
    result = 160.0 + 40*(la+la**2)    
    print("{:.3f}".format(result))
    
    result = 128.0 + 40*(lb+lb**2)    
    print("{:.3f}".format(result))
