#!/bin/python3

"""
groupby() function of itertools

https://docs.python.org/3/library/itertools.html

     
L = [("a", 1), ("a", 2), ("b", 3), ("b", 4), ("a", 5)] 
  
# Key function 
key_func = lambda x: x[0] 
  
for key, group in itertools.groupby(L, key_func): 
    print(key + " :", list(group)) 


Input:
1222311

Output:
(1, 1) (3, 2) (1, 3) (2, 1)

"""

from itertools import groupby

if __name__ == '__main__':
    
    l = list(map(lambda i:(int(i),1), input()))
    # print(l)
    
    # Key function 
    key_func0 = lambda x: x[0]
    key_func1 = lambda x: x[1] 
  
    print(*[(sum(list(map(key_func1, group))), key) 
            for key, group in groupby(l, key_func0)])        

