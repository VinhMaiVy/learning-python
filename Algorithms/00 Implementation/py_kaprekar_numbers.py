#!/bin/python3

"""
Input
1
100

Output
1 9 45 55 99

"""


def kaprekarNumbers(p, q):
    result = []
    for n in range(p,q+1):
        nlen = len(str(n))         
        nn = n*n
        if len(str(nn)) > nlen:
            lnn = int(str(nn)[:-nlen])
            rnn = int(str(nn)[-nlen:])
        else:
            lnn = rnn = nn
            if n == 1:
                result.append(n)
        if lnn + rnn == n:
                result.append(n)         
    if result:
        print(" ".join(map(str,result)))
    else:
        print('INVALID RANGE')
    
if __name__ == '__main__':
    p = int(input())
    q = int(input())
    kaprekarNumbers(p, q)
