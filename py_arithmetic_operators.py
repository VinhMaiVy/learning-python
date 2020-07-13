#!/bin/python

"""
Task
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers (first - second).
3. The third line contains the product of the two numbers.

Example
    a = 3
    b = 5
Print the following:
    8
    -2
    15

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

if __name__ == "__main__":
    # execute only if run as a script
    main()

