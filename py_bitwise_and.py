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
        max_c = 0
        list_c = list(combinations(list([i for i in range(1,n+1)]),2))
        for c in list_c:            
            if (c[0] & c[1]) < k:
                max_c = max(c[0] & c[1], max_c)            
        print(max_c)