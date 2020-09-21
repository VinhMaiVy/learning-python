#!/bin/python3

"""
Central Limit Theorem 3
Standard Normal Distribution
https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/tutorial


Input:
100
500
80
.95
1.96

Output:


"""

import math

if __name__ == '__main__':
    
    sample = float(input())   # 100
    mean = float(input())     # 500
    sigma = float(input())    # 80
    interval = float(input()) # 0.95
    z = float(input())        # 1.96
    
    sigma_sample = sigma / math.sqrt(sample)
    print("{:.2f}".format(mean - sigma_sample*z))
    print("{:.2f}".format(mean + sigma_sample*z))
    
    
