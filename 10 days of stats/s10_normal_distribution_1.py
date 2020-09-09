#!/bin/python3

"""
Normal Distribution
https://www.hackerrank.com/challenges/s10-normal-distribution-1/tutorial

Input:
20 2
19.5
20 22

Output:
0.401
0.341


"""

import math

def cum_distribution_function(x,_mean,_stddev):
    return 0.5*(1 + math.erf((x - _mean)/(_stddev * math.sqrt(2))))

if __name__ == '__main__':
    
    _mean, _stddev = list(map(float, input().rstrip().split()))
    lt = float(input())
    btw1, btw2 = list(map(float, input().rstrip().split()))
    
    result = cum_distribution_function(lt, _mean, _stddev)    
    print("{:.3f}".format(result))
    
    result = cum_distribution_function(btw2, _mean, _stddev) - cum_distribution_function(btw1, _mean, _stddev) 
    print("{:.3f}".format(result))
    

