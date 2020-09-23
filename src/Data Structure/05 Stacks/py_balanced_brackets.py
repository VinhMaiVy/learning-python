#!/bin/python3

"""
Python
Regular Expression

Input:
3
{[()]}
{[(])}
{{[[(())]]}}

Output:
YES
NO
YES

"""


import math
import os
import random
import re
import sys


# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    dic = {'{':'}', '[':']', '(':')'}
    for b in s:
        if b in '{[(':
            stack.append(dic[b])
        elif not stack or b != stack.pop():
            return 'NO'            
    return 'NO' if stack else 'YES'


def isBalanced2(s):
    p= "\[\]|\(\)|\{\}"
    while re.search(p,s):
        s = re.sub(p,"",s)
    return "NO" if s else "YES"


if __name__ == '__main__':

    t = int(input())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        print(result)
