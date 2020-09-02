#!/bin/python3

"""
Array Manipulation

Input:
5 3
1 2 100
2 5 100
3 4 100
Output:
200

Input:
10 3
1 5 3
4 8 7
6 9 1
Output:
10

"""



import math
import os
import random
import re
import sys
from array import array

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):    
    result = 0
    array = [0]*n
            
    for q in queries:
        a, b, k = q
        
        for i in range(a-1,b):
            array[i] += k
            if array[i] > result: # Find the maximum number
                result = array[i]
                            
    # print(array)
                    
    return result

if __name__ == '__main__':
    

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    
    # print(queries)
    result = arrayManipulation(n, queries)

    print(str(result) + '\n')
