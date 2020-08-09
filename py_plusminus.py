#!/bin/python3

def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    tot = len(arr)
    for n in arr:
        if n == 0:
           zer += 1
        elif n>0:
            pos += 1
        else:
            neg += 1
    print(pos, neg, zer, tot)
    print("{:.6f}".format(float(pos)/float(tot)))
    print("{:.6f}".format(float(neg) / float(tot)))
    print("{:.6f}".format(float(zer) / float(tot)))
    return

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
