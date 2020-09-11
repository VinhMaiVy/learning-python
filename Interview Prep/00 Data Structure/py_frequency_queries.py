#!/bin/python3

"""
Dictionary
List Comprehension

Input:
8
1 5
1 6
3 2
1 10
1 10
1 6
2 5
3 2
Output:
0
1

Input:
4
3 4
2 1003
1 16
3 1
Output:
0
1


Input:
10
1 3
2 3
3 2
1 4
1 5
1 5
1 4
3 2
2 4
3 2
Output:
0
1
1

"""


import math
import os
import random
import re
import sys

def freqQuery(queries):    
    dict1 = {}
    dict2 = {}    
    for q, n in queries:
        if q == 1:                                            
            if dict1.get(n,0) and dict2.get(dict1[n],[]):
                dict2[dict1[n]].remove(n)
                if not dict2[dict1[n]]:
                        del dict2[dict1[n]]
            dict1[n] = dict1.get(n,0) + 1                
            dict2[dict1[n]] = dict2.get(dict1[n],[]) + [n]            
            continue
        if q == 2:
            if dict1.get(n,0):                
                if dict2.get(dict1[n],[]):
                    dict2[dict1[n]].remove(n)
                    if not dict2[dict1[n]]:
                        del dict2[dict1[n]]
                dict1[n] -= 1
                if dict1[n]:
                    dict2[dict1[n]] = dict2.get(dict1[n],[]) + [n]
            continue
        if q == 3:
             yield 1 if n in dict2 else 0            

if __name__ == '__main__':

    q = int(input().strip())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
        
    #print(queries)
    ans = freqQuery(queries)
    
    print('\n'.join(map(str, ans)))
    print('\n')

    
