#!/bin/python3

"""
Python

Input:
95 85
85 95
80 70
70 65
60 70

Output:


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
    
    x = [0]*5
    y = [0]*5
    
    x[0], y[0] = list(map(float, input().split()))
    x[1], y[1] = list(map(float, input().split()))
    x[2], y[2] = list(map(float, input().split()))
    x[3], y[3] = list(map(float, input().split()))
    x[4], y[4] = list(map(float, input().split()))
    
    b = pearson_coef(x,y) * stddev(y) / stddev(x)
    a = mean(y) - b*mean(x)
    result = a + b*80.0
    
    print("{:.3f}".format( result ))
    
