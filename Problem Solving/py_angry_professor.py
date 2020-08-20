#!/bin/python3

"""
Input
2
4 3
-1 -3 4 2
4 2
0 -1 2 1

Output
YES
NO
"""

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    result = 'YES'
    present = sum(([1 for s in a if s <=0]))
    if present>=k:
        result = 'NO'
    return result

if __name__ == '__main__':
    

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        print(result + '\n')
