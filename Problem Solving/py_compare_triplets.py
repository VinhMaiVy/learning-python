#!/bin/python3

def compareTriplets(a, b):
    return [int(a[0]>b[0]) + int(a[1]>b[1]) + int(a[2]>b[2]), int(a[0]<b[0]) + int(a[1]<b[1]) + int(a[2]<b[2])]

if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    print(' '.join(map(str, result)))

