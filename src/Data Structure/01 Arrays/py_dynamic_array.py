#!/bin/python3

"""
Python

Input:
2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1

Output:
7
3

"""


import math
import os
import random
import re
import sys

def dynamicArray(n, queries):    
    last_answer = 0
    s = [[]]*n
    for q in queries:
        t, x, y = q
        if t == 1:
            fs = (x^last_answer) % n
            if s[fs]:
                s[fs].append(y)
            else:
                s[fs] = [y]
        elif t == 2:
            fs = (x^last_answer) % n
            last_answer = s[fs][y % len(s[fs])]
            yield last_answer
    
if __name__ == '__main__':
    

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print('\n'.join(map(str, result)))
    print('\n')
    
    
