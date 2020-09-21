#! /bin/python3


"""
Python

Input:
aaa Aaa bbb ccc aAa Bbb CCC
Output:


"""

# Complete the solve function below.

def solve(s):
    #return ' '.join(set(word.capitalize() for word in s.split(' ')))
    return ' '.join([word.capitalize() for word in s.split(' ')])

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)