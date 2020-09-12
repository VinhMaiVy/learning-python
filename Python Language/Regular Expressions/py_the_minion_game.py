#!/bin/python3

"""
Regular Expression
Strings manipulation

Input:
BANANA

Output:
Stuart 12





# finditer
[m.start() for m in re.finditer('test', 'test test test test')]
#[0, 5, 10, 15]

Overlapping matches
[m.start() for m in re.finditer('(?=tt)', 'ttt')]
#[0, 1]


Reverse find-all without overlaps
search = 'tt'
[m.start() for m in re.finditer('(?=%s)(?!.{1,%d}%s)' % (search, len(search)-1, search), 'ttt')]
#[1]


"""

import re

def minion_game(string):    
    kevin_score = 0
    stuart_score = 0
    
    len_s = len(string)

    kevin_matches = [m.start() for m in re.finditer('[AEIOU]', string)]        
    for i in kevin_matches:
        kevin_score += len_s - i

    stuart_matches = [m.start() for m in re.finditer('[B-DF-HJ-NP-TV-Z]', string)]            
    for j in stuart_matches:
        stuart_score += len_s - j
    
    if stuart_score == kevin_score:
        print('Draw')
    elif stuart_score > kevin_score:
        print('Stuart', stuart_score)        
    else:
        print('Kevin', kevin_score)        
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
    
