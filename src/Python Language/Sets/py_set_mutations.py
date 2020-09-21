#!/bin/python3

"""
Python

Input:
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66
 
Output:
38

"""

if __name__ == '__main__':
    
    na = int(input())
    a = set(map(int, input().rstrip().split()))
        
    n = int(input())
    for _ in range(n):
        c, nb = input().split()
        b = set(map(int, input().rstrip().split()))        
        # (c, b) = (input().split()[0], set(map(int, input().split())))
        eval('a.'+c+'(b)')
        # getattr(a, c)(b)
    
    print(sum(a))
        
         
