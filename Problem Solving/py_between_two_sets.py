#!/bin/python3

"""
Between Two Sets
lcm Least Common Multiple
Gcd Greasted Common Denominator
Hcf Highest Common Factor
Factor gcm lcm
Reduce

Input:
2 3
2 4
16 32 96

Output:
3 (4, 8, 16)

Input:
2 3
2 6
24 36

Output:
2 (6 12)

Input:
1 1
1
100
Output:
9

Input:
3 2
2 3 6
42 84
Output:
2

Input:
1 2
1
72 48

Output:
8


"""


import math
import os
import random
import re
import sys

from functools import reduce

def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(math.sqrt(n))+1, step) if n % i == 0)))

def gcd(a, b):
    if min(a, b) == 0:
        return max(a, b)
    a_1 = max(a, b) % min(a, b)
    return gcd(a_1, min(a, b))

def lcm(a, b):
    return (a * b) // gcd(a, b)

def getTotalX(a, b):
        
    a_lcm = reduce(lambda x, y: lcm(x,y), a)    
    b_hcf = reduce(lambda x, y: gcd(x,y), b)
        
    result = len([i for i in range(a_lcm, b_hcf+1) if not b_hcf%i and not i%a_lcm])            
    return(result)

    
if __name__ == '__main__':
    
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(str(total) + '\n')
    
