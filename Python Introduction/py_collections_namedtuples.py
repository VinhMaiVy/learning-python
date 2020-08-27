#!/bin/python3

"""
Python

Input:
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   
Output:
78.00

Input:
5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5
Output:
81.00

>>> from collections import namedtuple
>>> Car = namedtuple('Car','Price Mileage Colour Class')
>>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
>>> print xyz
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
>>> print xyz.Class
Y

"""

from collections import namedtuple

if __name__ == '__main__':        
    n = int(input())
    student_score = namedtuple('student_score', " ".join(input().rstrip().split()))    
    print("{:.2f}".format(sum([int(student_score(*(input().rstrip().split())).MARKS) for i in range(n)])/n))

    # n, Score = int(input()) , namedtuple('Score',input().split())
    # scores = [Score(*input().split()).MARKS for i in range(n)]
    # print("%.2f"% (sum(map(int,scores))/n))
        
    