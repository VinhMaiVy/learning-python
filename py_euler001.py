#!/bin/python3

"""
"""

if __name__ == '__main__':  
    
    t = int(input().strip())
    
    result = []    
    for a0 in range(t):
        n = int(input().strip())
        n3=int((n-1)/3)
        n5=int((n-1)/5)
        n15=int((n-1)/15)
        result.append(int(((3*n3*(n3+1)) >> 1) +
                       ((5*n5*(n5+1)) >> 1) - 
                       ((15*n15*(n15+1)) >> 1)))
    print('\n'.join(map(str, result)))
