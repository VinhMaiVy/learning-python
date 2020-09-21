#!/bin/python3

"""
Counter
Set

Input:
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
Output:


"""


from collections import Counter

if __name__ == '__main__':    
    k = int(input())
    a = list(map(int, input().rstrip().split()))
    ca = Counter(a)
    print(*[result for result in ca if ca[result] == 1])
