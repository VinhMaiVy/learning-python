#!/bin/python

"""

Given the participants' score sheet for your University Sports Day, you are required to find
the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

Sample Input:
5
2 3 6 6 5

Result:
5


"""

import math
import os
import random
import re
import sys

def main():
    sorted_arr = sorted(set(arr))
    print(sorted_arr[len(sorted_arr)-2])


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

if __name__ == "__main__":
    # execute only if run as a script
    main()