#!/bin/python3

def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True

if __name__ == '__main__':
    n = int(input())
    N = []
    for i in range(n):
        N.append(int(input()))

    for i in N:
        if isPrime(i):
            print('Prime')
        else:
            print('Not prime')