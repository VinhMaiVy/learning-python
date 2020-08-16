#!/bin/python

"""
Task
Given an integer n, perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

Input Format
A single line containing a positive integer,  n.  

Constraints
 1 <= n <=100

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.
"""


import math
import os
import random
import re
import sys


def main():
    if n % 2:
        print("Weird")
    else:
        if (n >= 6) and (n<=20):
            print("Weird")
        else:
            print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    main()

