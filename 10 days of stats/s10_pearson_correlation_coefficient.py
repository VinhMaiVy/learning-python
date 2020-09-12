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
    
    x, y = list(map(float, input().rstrip().split())), list(map(float, input().rstrip().split()))        

    result = pearson_coef(x,y)

    print("{:.3f}".format( result ))
