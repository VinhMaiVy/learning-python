#!/bin/python3

"""
Input
6
0 0 0 0 1 0
Output
3

Input
7
0 0 1 0 0 1 0
Output
4


"""

import math

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    result = 0
    cumulus = 0
    for thunderhead in c:
        if thunderhead:
            result += math.floor(cumulus/2)+1
            cumulus = 0
        else:
            cumulus += 1
    result += math.floor(cumulus/2)
    
    return result

if __name__ == '__main__':
    

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(str(result) + '\n')

    
