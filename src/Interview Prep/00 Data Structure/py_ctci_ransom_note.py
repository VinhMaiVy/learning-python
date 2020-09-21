#!/bin/python3

"""
Dictionary
Default Dictionary
Counter

Input:
6 4
give me one grand today night
give one grand today
Output:
Yes

Input:
6 5
two times three is not four
two times two is four
Output:
No

"""

import math
import os
import random
import re
import sys
from collections import defaultdict
from collections import Counter

def checkMagazine(magazine, note):
    if (Counter(note) - Counter(magazine)) == {}:
        print('Yes')
    else:
        print('No')

def checkMagazine1(magazine, note):
    result = 'Yes'
    
    magazine_dict = defaultdict(int)
    for m in magazine:
       magazine_dict[m] += 1
    
    for n in note:
        if n in magazine_dict:
            magazine_dict[n] -= 1
            if magazine_dict[n] == 0:
                del magazine_dict[n]
        else:
            result = 'No'
            break
    
    # print(magazine_dict)    
    print(result)
    

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
