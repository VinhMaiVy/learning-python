#!/bin/python3

"""
Median

Input:
9
3 7 8 5 12 14 21 13 18
Output:


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
    a = list(map(int, input().rstrip().split()))
    
    sa = sorted(a)
    med1, med2, med3 = [0]*3
    if (n % 2) == 0 and n>1:
        hn = n//2
        med1 = median(sa[:hn])
        med2 = (sa[hn]+sa[hn-1])/2
        med3 = median(sa[hn:])    
    elif n>2:
        hn = int(math.floor(n/2))
        med1 = median(sa[:hn])
        med2 = sa[hn]
        med3 = median(sa[-hn:])
        
    print(int(med1),int(med2),int(med3), sep='\n')
    