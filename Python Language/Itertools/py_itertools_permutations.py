#!/bin/python3

"""

itertools.permutations(iterable[, r])
Permutation
itertools
Print of list

>>> from itertools import permutations
>>> print permutations(['1','2','3'])
<itertools.permutations object at 0x02A45210>
>>> 
>>> print list(permutations(['1','2','3']))
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
>>> 
>>> print list(permutations(['1','2','3'],2))
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
>>>
>>> print list(permutations('abc',3))
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

Input:
HACK 2
Output:
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
"""

from itertools import permutations

if __name__ == '__main__':
    s, k = list(input().split())    
    for result in sorted(map("".join, list(permutations([c for c in s], int(k))))):
        print(result)
    
    # print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')

