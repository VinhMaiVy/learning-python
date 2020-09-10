#!/bin/python3

"""
Central Limit Theorem 2
Standard Normal Distribution
https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/tutorial

250 ticket left
100 students
mean = 2.4 tickets 
sigma = 2.0

Input:
250
100
2.4
2.0

Output:
0.6915

"""

import math

def cum_distribution_function(x,_mean,_stddev):
    return 0.5*(1 + math.erf((x - _mean)/(_stddev * math.sqrt(2))))

if __name__ == '__main__':
    
    max_tickets = float(input())
    nb_students = float(input())
    mean_tickets = float(input())
    sigma_tickets = float(input())
    
    mean_prime = nb_students * mean_tickets
    sigma_prime = math.sqrt(nb_students) * sigma_tickets
    
    #print(max_tickets, mean_prime, sigma_prime)
    result = cum_distribution_function(max_tickets, mean_prime, sigma_prime)
    
    print("{:.4f}".format(result))

    
