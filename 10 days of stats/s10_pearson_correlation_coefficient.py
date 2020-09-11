#!/bin/python3

"""
Pearson correlation coefficient

Input:
10
10 9.8 8 7.8 7.7 7 6 5 4 2 
200 44 32 24 22 17 15 12 8 4

Output:
0.612

"""

def mean(a):
    return sum(a)/(len(a))

def stddev(a):    
    return (sum([(n-mean(a))**2 for n in a])/n)**0.5

    
if __name__ == '__main__':
    
    n = int(input())
    
    x, y = list(map(float, input().rstrip().split())), list(map(float, input().rstrip().split()))        

    mx = mean(x)
    my = mean(y)
            
    result = sum([(x[i] - mx)*(y[i] - my) for i in range(n)]) / (n*stddev(x)*stddev(y))

    print("{:.3f}".format( result ))
