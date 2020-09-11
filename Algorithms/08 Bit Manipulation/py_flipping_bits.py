#!/bin/python3

"""
Input
3
2147483647
1
0

Output
2147483648
4294967294
4294967295

"""

def flippingBits(n):
    return int(''.join(['1' if b == '0' else '0' for b in '{:032b}'.format(n)]),2)

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        n = int(input())
        result = flippingBits(n)
        print(str(result) + '\n')