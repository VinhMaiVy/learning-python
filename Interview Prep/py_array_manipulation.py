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

Input:
40 30
19 28 419
4 23 680
5 6 907
19 33 582
5 9 880
10 13 438
21 39 294
13 18 678
12 26 528
15 30 261
8 9 48
21 23 131
20 21 7
13 40 65
13 23 901
15 15 914
14 35 704
20 39 522
10 18 379
16 27 8
25 40 536
5 9 190
17 20 809
8 20 453
22 37 298
19 37 112
2 5 186
21 29 184
23 30 625
2 8 960

OUtput:
6314

"""



import math
import os
import random
import re
import sys

from collections import Counter

def arrayManipulation1(n, queries):    
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
"""
Given a range[a, b] and a value k we need to add k to all the numbers whose indices are in the range from [a, b].
We can do an O(1) update by adding  to index a and add -k to index b+1.

Doing this kind of update, the ith  number in the array will be prefix sum of array from index 1 to i because we are 
adding k to the value at index b+1 and subtracting from the value at index  and taking prefix sum will give us the 
actual value for each index after m operations .

So, we can do all m updates in O(m) time. Now we have to check the largest number in the original array. i.e. the 
index i such that prefix sum attains the maximum value.

We can calculate all prefix sums as well as maximum prefix sum in O(n) time which will execute in time.
"""

def arrayManipulation(n, queries):
    arrSum = 0
    maxSum = 0
    c = Counter()
    
    for a,b,k in queries:
        c[a]  +=k
        c[b+1]-=k
    
    for i in sorted(c)[:-1]:
        arrSum+= c[i]
        maxSum = max(maxSum,arrSum)
        
    return maxSum       

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
