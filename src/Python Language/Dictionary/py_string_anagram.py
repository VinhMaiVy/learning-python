#!/bin/python3

"""
Python

Input:
12
hack
a
rank
khac
ackh
kran
rankhacker
a
ab
ba
stairs
raits
5
a
nark
bs
hack
stair

Output:


"""

import math
import os
import random
import re
import sys



#
# Complete the 'stringAnagram' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#


def stringAnagram(dictionary, query):
    
    s_dictionary = {}    
    for d in dictionary:
        k = "".join(sorted(d))
        s_dictionary[k] = s_dictionary.get(k,0) + 1
        
    for word in query:
        k = "".join(sorted(word))
        yield s_dictionary[k] if k in s_dictionary else 0 


if __name__ == '__main__':
    
    dictionary_count = int(input().strip())

    dictionary = []

    for _ in range(dictionary_count):
        dictionary_item = input()
        dictionary.append(dictionary_item)

    query_count = int(input().strip())

    query = []

    for _ in range(query_count):
        query_item = input()
        query.append(query_item)

    result = stringAnagram(dictionary, query)

    print('\n'.join(map(str, result)))
    print('\n')
