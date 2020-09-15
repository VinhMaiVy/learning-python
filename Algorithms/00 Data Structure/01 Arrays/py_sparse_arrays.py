#!/bin/python3

"""
Arrays
Counters

Input:
13
abcde
sdaklfj
asdjf
na
basdn
sdaklfj
asdjf
na
asdjf
na
basdn
sdaklfj
asdjf
5
abcde
sdaklfj
asdjf
na
basdn

Output:
1
3
4
3
2

"""

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    d = {}
    for s in strings:
        d[s] = d.get(s,0) + 1
    
    for q in queries:
        if q in d:
            yield d[q]
        else:
            yield 0

def matchingStrings2(strings, queries):
    c = Counter(strings)
    return (c[i] for i in queries)

if __name__ == '__main__':
    

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    print('\n'.join(map(str, res)))
    print('\n')
