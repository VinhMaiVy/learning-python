#!/bin/python3

"""
Python

Input:
5
95 85
85 95
80 70
70 65
60 70
80

Output:
78.288

Input:
10
15 10
12 25
8 17
8 11
7 13
7 17
7 20
6 13
5 9
3 15
10

"""

def mean(x):
    return sum(x)/(len(x))

def stddev(x):
    mx = mean(x)    
    return (sum([(i-mx)**2 for i in x])/len(x))**0.5

def pearson_coef(x,y):
    mx = mean(x)
    my = mean(y)
    n = len(x)
    return sum([(x[i] - mx)*(y[i] - my) for i in range(n)]) / ( n * stddev(x) * stddev(y) )

if __name__ == '__main__':
    
    n = int(input())
    x = [0.0]*n
    y = [0.0]*n
    for i in range(n):
        x[i], y[i] = list(map(float, input().rstrip().split()))

    fs_x = float(input())
            
    b = pearson_coef(x,y) * stddev(y) / stddev(x)
    a = mean(y) - b*mean(x)
    result = a + b*fs_x
    
    print("a={:.3f}".format( a ))
    print("b={:.3f}".format( b ))
    print("fs_y={:.3f}".format( result ))
    
