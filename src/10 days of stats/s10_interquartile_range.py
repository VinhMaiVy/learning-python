#!/bin/python3

"""
Inter-quartile Range

Input:
6
6 12 8 10 20 16
5 4 3 2 1 5
Output:
9.0


"""
import math

def median(sa):
    n = len(sa)    
    if (n % 2) == 0:
        return (sa[n//2]+sa[n//2-1])/2
    else:
        return sa[math.floor(n/2)]
        
if __name__ == '__main__':
    
    n = int(input())
    x = list(map(int, input().rstrip().split()))
    f = list(map(int, input().rstrip().split()))
    
    a = []
    for i in range(n):
        a += [x[i]]*f[i]    
    sa = sorted(a)
    n = len(sa)
    #print(sa)
    
    med1, med3 = [0]*2
    if (n % 2) == 0 and n>1:
        hn = n//2
        med1 = median(sa[:hn])        
        med3 = median(sa[hn:])    
    elif n>2:
        hn = int(math.floor(n/2))
        med1 = median(sa[:hn])
        med3 = median(sa[-hn:])
        
    print("{:.1f}".format( float( med3-med1 ) ) )

    