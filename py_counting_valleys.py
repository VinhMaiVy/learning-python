#!/bin/python3


def countingValleys(n, s):
    altitude = 0
    valleys = 0

    c: str
    for c in s:
        if c=='U':
            altitude +=1
            if (altitude == 0):
                valleys += 1
        else:
            altitude -=1
    return valleys

if __name__ == '__main__':

    n = int(input())
    s = input()
    result = countingValleys(n, s)
    print(result)