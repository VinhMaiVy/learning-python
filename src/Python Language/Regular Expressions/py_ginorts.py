#!/bin/python3

"""
Regular Expression
Sorting Key Index

Input:
Sorting1234
1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0pQWERTYUIOPASDFGHJKLZXCVBNM

Output:
ginortS1324
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468
"""

import re

if __name__ == '__main__':
    
    s = "".join(sorted(input()))
    print("".join(re.findall('[a-z]',s))+"".join(re.findall('[A-Z]',s))+
          "".join(re.findall('[13579]',s))+"".join(re.findall('[02468]',s)))
    
    #order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
    #print(*sorted(input(), key=order.index), sep='')
    