#!/bin/python3

"""

Input 
10 2 3
3 1
5 2 8

Output
9

"""

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    moneySpent = -1
    
    for k in keyboards:
        for d in drives:             
             if moneySpent <= (k+d) <= b:
                 moneySpent = k+d
    
    return moneySpent

if __name__ == '__main__':
    
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(str(moneySpent) + '\n')
