#!/bin/python3

"""
Geometric Distribution 2
https://www.hackerrank.com/challenges/s10-geometric-distribution-1/tutorial

Input:
1 3
5

Output:

"""

import math

def combination(n,x):
    return (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))

def negative_binomial_distribution(x, n, p):
    # return math.comb(n,x)*(p**x)*((1-p)**(n-x))
    return combination(n-1,x-1)*(p**x)*((1.0-p)**(n-x))


if __name__ == '__main__':
    
    (pn, pd) = list(map(int, input().split()))
    
    p = pn / pd
    q = 1.0 - p
    
    n = int(input())
            
    result = sum([q**(n-1) * p for n in range(1,6)])
             
    print("{:.3f}".format(result))
