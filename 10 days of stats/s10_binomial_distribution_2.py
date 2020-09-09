#!/bin/python3

"""
Binomial Distribution 2
https://www.hackerrank.com/challenges/s10-binomial-distribution-1/tutorial

Input:
12 10

Output:
0.891
0.342

"""

import math


def combination(n,x):
    return (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))

def binomial_distribution(x, n, p):
    # return math.comb(n,x)*(p**x)*((1-p)**(n-x))
    return combination(n,x)*(p**x)*((1.0-p)**(n-x))


if __name__ == '__main__':
    
    d, n = input().split()
    d, n = float(d), int(n)
    p = d/100.0
    
    result = 0
    for x in range(3): # 0,1,2
        result += binomial_distribution(x, n, p)         
    print("No more than 2 rejects: {:.3f}".format(result))
    
    result = 0
    for x in range(2,n+1): # 2,3,4,5,6,7,8,9,10
        result += binomial_distribution(x, n, p)         
    print("At least 2 rejects: {:.3f}".format(result))
    
