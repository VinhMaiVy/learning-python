#!/bin/python3

"""

itertools.product()
itertools
product

Input:
1 2
3 4

Ouput:
(1, 3) (1, 4) (2, 3) (2, 4)

"""

from itertools import product

if __name__ == '__main__':
    
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    
    result = list(product(a,b))
    
    print(" ".join([str(i) for i in result]))
        
    