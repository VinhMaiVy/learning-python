#!/bin/python3

"""
itertools

https://realpython.com/python-itertools/

"""

import itertools

if __name__ == '__main__':    
    print(*itertools.combinations([1, 2, 3], 2))
    
    print(*itertools.combinations_with_replacement([1, 2], 2))
    
    print(*itertools.permutations('abc'))
    
    
    counter = itertools.count()
    print(*list(next(counter) for _ in range(5)))
    
    evens = itertools.count(step=2)
    print(*list(next(evens) for _ in range(5)))
    
    odds = it.count(start=1, step=2)
    print(*list(next(odds) for _ in range(5)))