#!/bin/python3

"""

Input:

7 3
Tsi
h%x
i #
s $
$a$
#t%
ir!

Output:
This is Matrix#  %!

"""

import re

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    matrix = []
    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    decoded = ''
    for i in range(m):
        for j in matrix:
            decoded = decoded + j[i]

    print(decoded)
    decoded = re.sub(r'\b[^a-zA-Z0-9]+\b', r' ',decoded)
    print(decoded)