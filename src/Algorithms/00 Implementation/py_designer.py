#!/bin/python3

"""
Python

Input:
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
zaba

Output:
28

"""

import math
import os
import random
import re
import sys


def designerPdfViewer(h, word):
    d = {}
    maxheight = 0
    for i in range(len(h)):
        d[i + 97] = h[i]
    for w in word:
        maxheight = max(maxheight, d[ord(w)])
    return maxheight * len(word)


if __name__ == '__main__':

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(str(result) + '\n')

