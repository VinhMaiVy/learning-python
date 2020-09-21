#!/bin/python3

"""
Normal Distribution
https://www.hackerrank.com/challenges/s10-normal-distribution-1/tutorial

Input:
70 10
80
60

Output:
0.401
0.341


"""

import math

def cum_distribution_function(x,_mean,_stddev):
    return 0.5*(1 + math.erf((x - _mean)/(_stddev * math.sqrt(2))))

if __name__ == '__main__':
    
    _mean, _stddev = list(map(float, input().rstrip().split()))
    h80 = float(input())
    p60 = float(input())
    
    
    result = 100.0*(1 - cum_distribution_function(h80, _mean, _stddev))    
    print("{:2.2f}".format(result))
    
    result = 100.0*(1 - cum_distribution_function(p60, _mean, _stddev))    
    print("{:2.2f}".format(result))
    print("{:2.2f}".format(100.0-result))
    

    

