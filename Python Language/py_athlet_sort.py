#!/bin/python3

"""
Sort using Lambda

Input:
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

Output:
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

"""

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    k = int(input())
    l = lambda x: x[k]    
    for row in sorted(arr, key = l):
        print(*row, sep = " ")
