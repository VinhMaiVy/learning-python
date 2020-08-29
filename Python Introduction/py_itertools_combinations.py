#!/bin/python3

"""
combinations

>>> from itertools import combinations
>>>
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4',
'5')]
>>>
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]


Input:
HACK 2

Output:
A
C
H
K
AC
AH
AK
CH
CK
HK


"""

from itertools import combinations

if __name__ == '__main__':
       
    s, k = list(input().split())
    k = int(k)
    s = sorted(s)
    combi_s = []    
    for _ in range(1,k+1):
        combi_s += sorted(list(map(lambda x: "".join(x), combinations(s,_))))
    
    print(*combi_s, sep = "\n")
    

