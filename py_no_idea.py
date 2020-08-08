#! /bin/python

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    N = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]

    hapiness = 0

    for _ in range(n):
        if N[_] in A:
            hapiness += hapiness
        if N[_] in B:
            hapiness -= hapiness

    print(hapiness)