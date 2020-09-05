#!/bin/python3


"""
Sort

Input:
4
4 3 1 2
Output:
3

Input:
5
2 3 4 1 5
Output:
3

"""

import math
import os
import random
import re
import sys

def minimumSwaps(arr):
    result = 0
    len_a = len(arr)
    is_visited = [False]*len_a 
    
    for n in range(len_a):
    
        if not is_visited[n]:
            is_visited[n] = True
            
        if (arr[n] == n+1):
            continue
        else:
            c = arr[n]-1
            while (not is_visited[c]):
                is_visited[c] = True
                c = arr[c]-1
                result +=1
        
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    #print(arr)    
    res = minimumSwaps(arr)
    print(str(res) + '\n')

