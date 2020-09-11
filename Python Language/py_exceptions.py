#!/bin/python3

"""
Exception
Formating Fload

Input:
3
1 0
2 $
3 1

Output:
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3

"""

if __name__ == '__main__':
    
    n = int(input())
    for _ in range(n):
        try:
            a, b = list(map(int, input().rstrip().split()))
            result = a//b
        except Exception as e:
            print('Error Code:', e)            
        else:
            print('{0:g}'.format(result))
