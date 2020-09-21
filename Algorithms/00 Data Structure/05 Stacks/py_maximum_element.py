#!/bin/python3

"""
Python

Input:
10
1 97
2
1 20
2
1 26
1 20
2
3
1 91
3

Output:
26
91

"""



if __name__ == '__main__':
    
    n = int(input())
    stack = deque()
    counter = {}
    maxn = 0
    
    for _ in range(n):        
        c, *a = list(map(int, input().split()))
        
        if c == 1:
            last = a[0]
            stack.append(last)            
            counter[last] = counter.get(last,0) + 1
            if last > maxn:
                maxn = last
                            
        elif c == 2:            
            last = stack.pop()
            counter[last] -= 1
            if counter[last] == 0:                 
                del counter[last]
                if last == maxn:
                    if counter:
                        maxn = max(counter)
                    else:
                        maxn = 0
                    
        elif c == 3:
            print(maxn)

