#!/bin/python3

import sys

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))

    totalNbOfSwaps = 0
    for i in range(n):

        # Track number of elements swapped during a single array traversal
        numberOfSwaps = 0

        for j in range(n - 1):
            # Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                numberOfSwaps += 1
                totalNbOfSwaps += 1

        # If no elements were swapped during a traversal, array is sorted
        if (numberOfSwaps == 0):
            break

    print('Array is sorted in {} swaps.'.format(totalNbOfSwaps))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[len(a) - 1]))