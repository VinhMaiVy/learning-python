#!/bin/python3

"""
Input
3 2 3
1 2 3
0
1
2

Output
2
3
1

Input
3 2 2
3 2 5
1
2

Output
5
3
"""

def circularArrayRotationQuery(a, k, i, l):
    index = (i-k) % l
    result = a[index]     
    return result

def circularArrayRotation(a, k, queries):
    result = []
    for i in queries:
        result.append(circularArrayRotationQuery(a, k, i, len(a)))
    return result

if __name__ == '__main__':    

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    print('\n'.join(map(str, result)))
    print('\n')

    
