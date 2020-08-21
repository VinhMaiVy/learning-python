#!/bin/python3

"""

Input
11
1 2 3 4 5 4 3 2 1 3 4

Output
3

"""


def migratoryBirds(arr):
    birds = {}
    for b in arr:
        if b in birds:
            birds[b] += 1
        else:
            birds[b] = 1

    result = -1
    bmax = -1
    for b in birds:
        if birds[b] > bmax:
            bmax = birds[b]
            result = b
        elif (birds[b] == bmax) and (b < result):
            result = b
                        
    return result

if __name__ == '__main__':

    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    print(str(result) + '\n')


