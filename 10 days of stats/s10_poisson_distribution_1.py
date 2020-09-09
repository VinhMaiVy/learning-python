#!/bin/python3

"""
Poisson Distribution 1
https://www.hackerrank.com/challenges/s10-poisson-distribution-1/tutorial

Input:
3
2

Output:
0.180

"""

import math

def poisson_distribution(k,l):
    return (l**k)*math.exp(-l)/math.factorial(k)

if __name__ == '__main__':
    
    l = float(input())
    k = int(input())
    
    result = poisson_distribution(k,l)
             
    print("{:.3f}".format(result))
