#!/bin/python3

"""
Python

Input:
5 2
a
a
b
a
b
a
b
Output:
1 2 4
3 5

from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i
    
('python', ['awesome', 'language'])
('something-else', ['not relevant'])


"""

from collections import defaultdict

if __name__ == '__main__':
    
    a_dict = defaultdict(list)
    
    n,m = list(map(int, input().split()))
    
    
    for i in range(n):
        a_dict[input()].append(i+1)
        
    for i in range(m):
        b = input()
        print(*(a_dict[b] if a_dict[b] else [-1]))
                        
        
    
        