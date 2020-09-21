#!/bin/python3

"""
Python

Input:
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 

Output:
206

Input:
6 767
2 488512261 423332742
2 625040505 443232774
1 4553600
4 92134264 617699202 124100179 337650738
2 778493847 932097163
5 489894997 496724555 693361712 935903331 518538304

Output:
763


"""

from itertools import product

if __name__ == '__main__':    
    k, n = list(map(int, input().split()))
    K = [list(map(lambda N: int(N)**2, input().split()))[1:] for i in range(k)]
    print(max([sum(N)%n for N in list(product(*K))]))
    