#!/bin/python3

"""
Regular Expression
Strings manipulation

Input
BANANA

Output
Stuart 12

"""


def minion_game(string):    
    kevin_score = 0
    stuart_score = 0
    
    if stuart_score >= kevin_score:
        print('Stuart', stuart_score)
    else:
        print('Kevin', kevin_score)

if __name__ == '__main__':
    s = input()
    minion_game(s)