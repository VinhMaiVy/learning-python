#!/bin/python3

"""
Recursion

Input:

Output:


"""

def fibonacci(n):
    return n if (n == 0) or (n == 1) else fibonacci(n-1) + fibonacci(n-2) 

if __name__ == '__main__':
    
    n = int(input())
    print(fibonacci(n))
