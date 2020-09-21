#!/bin/python3

"""
Pearson correlation coefficient

Input:
2 7
0.18 0.89 109.85
1.0 0.26 155.72
0.92 0.11 137.66
0.07 0.37 76.17
0.85 0.16 139.75
0.99 0.41 162.6
0.87 0.47 151.77
4
0.49 0.18
0.57 0.83
0.56 0.64
0.76 0.18

Output:
105.22
142.68
132.94
129.71

"""
from sklearn import linear_model

if __name__ == '__main__':
    m, n = list(map(int, input().split()))
    
    x = []
    y = []
    
    for _ in range(n):
        x_y = list(map(float, input().rstrip().split()))
        x.append(x_y[:m])
        y.append(x_y[m])
        
    #print(x)
    #print(y)
    lm = linear_model.LinearRegression()
    lm.fit(x, y)
    a = lm.intercept_
    b = lm.coef_
    #print(a, b[0], b[1])
        
    q = int(input())    
    fs_x = []
    for _ in range(q):
        fs_x = list(map(float, input().rstrip().split()))
        fs_y = a + sum([b[i]*fs_x[i] for i in range(m)])
        print("{:.2f}".format( fs_y ))
        
        
    
 