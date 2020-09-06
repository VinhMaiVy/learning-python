#!/bin/python3

"""
Input:
rUns dOg

Output:
DoG RuNS
"""

import math
import os
import random
import re
import sys



def reverse_words_order_and_swap_cases(sentence):
    result = sentence.split()
    return " ".join([result[w].swapcase() for w in range(len(result)-1,-1,-1)])
    

if __name__ == '__main__':
    
    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)
    
    print(result + '\n')
