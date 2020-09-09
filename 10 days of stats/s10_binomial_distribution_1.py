#!/bin/python3

"""
Binomial Distribution 1
https://www.hackerrank.com/challenges/s10-binomial-distribution-1/tutorial


Input:
1.09 1

Output:
0.696

"""

import math

def combination(n,x):
    return (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))

def binomial_distribution(x, n, p):
    # return math.comb(n,x)*(p**x)*((1-p)**(n-x))
    return combination(n,x)*(p**x)*((1.0-p)**(n-x))

if __name__ == '__main__':
    
    (b, g) = list(map(float, input().split()))    
    q = g/(b+g)
    p = 1.0-q
    n = 6
    
    result = 0.0
    for x in range(3,n+1): # 3,4,5,6
        result += binomial_distribution(x, n, p)         

    print("{:.3f}".format(result))
