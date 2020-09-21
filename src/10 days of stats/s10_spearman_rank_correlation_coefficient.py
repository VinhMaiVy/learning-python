#!/bin/python3

"""
Pearson correlation coefficient

Input:
10
10 9.8 8 7.8 7.7 1.7 6 5 1.4 2 
200 44 32 24 22 17 15 12 8 4

Output:
0.903

"""

def mean(a):
    return sum(a)/(len(a))

def stddev(a):    
    return (sum([(n-mean(a))**2 for n in a])/n)**0.5

def ranked(a):
    r = {}
    _sa_ = sorted(a) 
    for i in range(len(a)):
        r[_sa_[i]] = i + 1 
    return r
    
if __name__ == '__main__':
    
    n = int(input())
    
    x, y = list(map(float, input().rstrip().split())), list(map(float, input().rstrip().split()))        
        
    rx, ry  = ranked(x), ranked(y)    

    sum_di_sq = sum([(rx[x[i]] - ry[y[i]])**2 for i in range(n)]) 
        
    result = 1 - (6 * sum_di_sq / (n*(n**2-1)))

    print("{:.3f}".format( result ))
    