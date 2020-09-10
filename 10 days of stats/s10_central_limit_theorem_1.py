#!/bin/python3

"""
Central Limit Theorem 1
Standard Normal Distribution
https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/tutorial

9800 (lbs)
49 boxes

mean = 205 (lbs)
sigma = 15 

Input:
9800
49
205
15

Output:
0.0098

"""

import math

def cum_distribution_function(x,_mean,_stddev):
    return 0.5*(1 + math.erf((x - _mean)/(_stddev * math.sqrt(2))))

if __name__ == '__main__':
    
    max_weight = float(input())
    nb_boxes = float(input())
    mean_weight_boxes = float(input())
    sigma_weight_boxes = float(input())
    
    mean_prime = nb_boxes * mean_weight_boxes
    sigma_prime = math.sqrt(nb_boxes) * sigma_weight_boxes
    # print(max_weight, mean_prime, sigma_prime)
    result = cum_distribution_function(max_weight, mean_prime, sigma_prime)
    
    print("{:.4f}".format(result))

    
