#!/bin/python3

"""
Sort

Input:
7 50
1 12 5 111 200 1000 10

Output:
4

"""


import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):    
    result = 0
    buy = 0        
    s_prices = sorted(prices)
    
    for t in s_prices:        
        buy += t
        if buy > k:
            break
        result += 1
                            
    return result

if __name__ == '__main__':
    

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    print(str(result) + '\n')


