#! /bin/python

"""

Nested Logfic

9 6 2015
6 6 2015

5 6 2015
6 6 2015

31 12 2009
1 1 2010

"""

if __name__ == '__main__':
               
    d2, m2, y2 = list(map(int, input().split())) # Return date
    d1, m1, y1 = list(map(int, input().split())) # Due date  
    
    result=0
    
    if y2>y1:
        result = 10000
    elif (y2==y1) and (m2>m1):
        result = 500*(m2-m1)
    elif (y2==y1) and (m2==m1) and (d2>d1):
        result = 15*(d2-d1)
    
    print(result)
