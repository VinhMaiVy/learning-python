#!/bin/python3

"""
List Comprehension

Input:
5
10 40 30 50 20
1 2 3 4 5
Output:
32.0

"""

if __name__ == '__main__':    
    n = int(input())
    x = list(map(int, input().rstrip().split()))
    w = list(map(int, input().rstrip().split()))
    print("{:.1f}".format( sum([x[i]*w[i] for i in range(len(x))])/sum(w) ))