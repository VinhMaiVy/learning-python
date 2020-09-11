#!/bin/python3

"""

7 11
5 15
3 2
-2 2 1
5 -6

"""
from _socket import AF_APPLETALK

def countApplesAndOranges(s, t, a, b, apples, oranges):
    af = 0
    for _ in apples:
        if s <= a+_ <= t:
            af += 1
    print(af)
    
    of = 0
    for _ in oranges:
        if s <= b+_ <= t:
            of += 1
    print(of) 
    
def countApplesAndOranges2(s, t, a, b, apples, oranges):
    print(sum([1 for x in apples if s <= (x + a) <= t]))
    print(sum([1 for x in oranges if s <= (x + b) <= t])) 
    


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
    countApplesAndOranges2(s, t, a, b, apples, oranges)
