#!/bin/python3

"""

3
5 2
8 5
2 2

"""

from itertools import combinations

if __name__ == '__main__':
    
    t = int(input())

    list_nk = []    
    
    for t_itr in range(t):
        nk = input().split()
        list_nk.append((int(nk[0]), int(nk[1])))        
                
    for nk in list_nk:
        n = nk[0]
        k = nk[1]
        if (k & 1):
            print(k-1)            
        else:
            if n > k:
                print(k+1 & k-1)
            else:                
                print(k-1 & k-2)