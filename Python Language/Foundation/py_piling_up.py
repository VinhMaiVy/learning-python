#!/bin/python3

"""
Python

Input:
2
6
4 3 2 1 3 4
3
1 3 2

Output:
Yes
No


Input:
1
3
1 3 2

Output:
No


"""


def canPile(n,l):
    result = False

    if l[0] >= l[-1]:
        last = l[0]
    else:
        last = l[-1]
        
    while l:
        if last >= l[0] >= l[-1]:
            last = l[0]
            del l[0]
        elif last >= l[-1] > l[0]:
            last = l[-1]
            del l[-1]
        else:
            break
                                
    return False if l else True 

    
if __name__ == '__main__':
    
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        l = list(map(int, input().split()))
        if canPile(n, l):
            print('Yes')
        else:
            print('No')
