#!/bin/python3

"""
Geometric Distribution 1
https://www.hackerrank.com/challenges/s10-geometric-distribution-1/tutorial

Input:
1 3
5

Output:

"""

if __name__ == '__main__':
    
    (pn, pd) = list(map(int, input().split()))
    
    p = pn / pd
    q = 1.0 - p
    
    n = int(input())
            
    result = q**(n-1) * p
             
    print("{:.3f}".format(result))
