#!/bin/python3

"""
Python

Input:
9
1 2 3 4 5 6 7 9 8
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

Output:
4

"""



if __name__ == '__main__':
    
    n = int(input())
    s = set(map(int, input().split()))
    
    N = int(input())
    for _ in range(N):
        cmd, *args = input().split()
        if args:
            getattr(s, cmd)(int(args[0]))
        else:
            getattr(s, cmd)()
        
        # eval('s.{0}({1})'.format(*input().split()+['']))
        
    print(sum(s))
