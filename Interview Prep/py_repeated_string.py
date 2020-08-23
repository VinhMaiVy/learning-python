#!/bin/python3

"""

Intput:
aba
10
Output:
7


"""

import re
import math 

def repeatedString(s, n):
    len_s = len(s)
    result =  len(re.findall('a',s))*math.floor(n/len_s) 
    result += len(re.findall('a', s[:(n % len_s)]))        
    return result

if __name__ == '__main__':
    
    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(str(result) + '\n')
