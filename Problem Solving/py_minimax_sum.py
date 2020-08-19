#!/bin/python3

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    print(sum(sorted(arr)[0:4]), sum(sorted(arr)[1:5]))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
