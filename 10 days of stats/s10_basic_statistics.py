#!/bin/python3

"""
Mean, Median, Mode

Input:
10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

Output:
43900.6
44627.5
4978

"""

import math
from collections import Counter

if __name__ == '__main__':
    
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    print("{:.1f}".format(float(sum(a)/n)))
    
    sa = sorted(a)
    if (n % 2) == 0 and n>1:
        print("{:.1f}".format( float( (sa[n//2]+sa[n//2-1])/2 ) ))
    elif n>2:
        print("{:.1f}".format( float( (sa[math.floor(n/2)]) )))
    else:
        print("{:.1f}".format( float( (sa[0] ) )))
    
    ca = Counter(a)
    max_ca = max(ca.values())
    print(min([n for n in ca if ca[n] == max_ca]))