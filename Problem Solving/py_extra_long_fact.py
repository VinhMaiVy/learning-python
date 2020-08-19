#!/bin/python3

def extraLongFactorials(n):
    fac = 1
    for i in range(2,n+1):
        fac *= i
    print(fac)

if __name__ == '__main__':
    n = int(input())
    extraLongFactorials(n)
