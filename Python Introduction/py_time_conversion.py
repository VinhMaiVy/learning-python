#!/bin/python3

"""
Input
07:05:45PM
12:05:45AM

Output
19:05:45
00:05:45
"""

def timeConversion(S):
    h, m, s = map(int, S[:-2].split(':'))
    p = S[-2:]
    h = h % 12 + (p.upper() == 'PM') * 12
    return (('%02d:%02d:%02d') % (h, m, s))


if __name__ == '__main__':
    S = input()
    result = timeConversion(S)
    print(result)
