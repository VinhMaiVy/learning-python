#! /bin/python

"""

No Idea

Input:
3 2
1 5 3
3 1
5 7

Output:
1

"""

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    N = [int(i) for i in input().split()]
    A = set([int(i) for i in input().split()])
    B = set([int(i) for i in input().split()])

    hapiness = 0

    for _ in range(n):
        if N[_] in A:
            hapiness += 1
        if N[_] in B:
            hapiness -= 1

    print(hapiness)

# or print(sum([(i in A) - (i in B) for i in N]))
