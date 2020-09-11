#!/bin/python3

"""

collections.Counter()

>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]

Input:
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Output:
200

"""

from collections import Counter

if __name__ == '__main__':
    X = int(input()) # Number of shoes    
    Xs = list(map(int, input().rstrip().split())) # Shoe sizes
    Cs = Counter(Xs)
    
    N = int(input()) # Number of customer
    
    result = 0
    for n in range(N): 
        s, p = list(map(int, input().rstrip().split()))
        if Cs[s]:
            result += p            
            if Cs[s] - 1 == 0:
                del Cs[s]
            else:
                Cs[s] -= 1
            
    print(result)