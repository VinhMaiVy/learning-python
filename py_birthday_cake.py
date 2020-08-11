#!/bin/python3

def birthdayCakeCandles(ar):
    sorted_ar = sorted(ar)
    return sorted_ar.count(sorted_ar[len(sorted_ar)-1])

if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
    print(result)