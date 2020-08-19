#!/bin/python3

def timeConversion(S):
    h, m, s = map(int, S[:-2].split(':'))
    p = S[-2:]
    h = h % 12 + (p.upper() == 'PM') * 12
    return (('%02d:%02d:%02d') % (h, m, s))


if __name__ == '__main__':
    S = input()
    result = timeConversion(S)
    print(result)
